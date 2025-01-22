#include <ArduinoJson.h>
#include "incbin.h"

// using incbin: https://github.com/AlexIII/incbin-arduino
INCTXT(ConfigFile, "clock_config.json");

typedef struct square_wave {
    bool enabled; // whether this wave is enabled
    int period; // x 100us = period (s)  
    int duty; // x 100us = duration high
    int phase; // x 100us = offset
    bool polarity; // start high or low
    int counter=0; //this is what Dr. Dahl called 'clock'
    int state=0; // internal variable for whether it is currently high or low
   } Square_Wave;
Square_Wave waves[16];

bool delayRunning = false; // true if still waiting for delay to finish
int DELAY_TIME = 100; // 10 us
unsigned long delayStart = 0; // the time the delay started
unsigned long prevTime = 0;

unsigned long powers[16];
unsigned long waveMask = 0; // which pins should be high
unsigned long wave_const = 0b11111111111111111; // 16 bit mask

void setup(void) {
  Serial.begin(9600);
  while (!Serial) continue;

  // powers of 2, using bit shifting
  unsigned long base = 0b1;
  for (int i=0; i<16; i++) {powers[i] = base<<i;}
  
  // rail C and L set to output
  DDRC = B11111111; // digital pin 37-30
  DDRL = B11111111;  // digital pin 49-42

  // deserialize the json file text to a json object
  JsonDocument conf;
  DeserializationError error = deserializeJson(conf, gConfigFileData);

  if (error){
    Serial.println(F("Failed to read file"));
    Serial.println(error.c_str());
    return;
  }

  // extract from json object to square_wave class
  Serial.println("Wave\tEnabled\tPeriod\tPhase\tDuty\tPolarity");
  for (JsonPair kv : conf.as<JsonObject>()) {
    const char* key = kv.key().c_str();
    int wave_num;
    if (sscanf(key, "wave%d", &wave_num) <=0) {
      continue; // continue if not wave#
    }
    wave_num -= 1;
    JsonObject v = kv.value().as<JsonObject>();
    waves[wave_num].enabled = v["enabled"].as<bool>();
    waves[wave_num].period = v["period"].as<int>();
    waves[wave_num].duty = v["duty"].as<int>() * waves[wave_num].period / 100;  // convert percentage to time
    waves[wave_num].phase = v["phase"].as<int>() * waves[wave_num].period / 100;  // convert percentage to time
    waves[wave_num].polarity = v["polarity"].as<bool>();
    Serial.print(wave_num); Serial.print("\t");
    waves[wave_num].enabled ? Serial.print("yes\t") : Serial.print("no\t");
    Serial.print(waves[wave_num].period); Serial.print("\t");
    Serial.print(waves[wave_num].phase); Serial.print("\t");
    Serial.print(waves[wave_num].duty); Serial.print("\t");
    Serial.print(waves[wave_num].polarity); Serial.print("\n");
  }
  delayStart = micros();
}

void loop(void) {  
  //Waves:
  for(int w=0; w<16; w++){
    Square_Wave* wave = &waves[w];
    if (wave->enabled < 1) {
      continue; // skip if not enabled
    }
    if (wave->state==0 && wave->counter > wave->phase){
      wave->state = 1;
    }
    else if (wave->state==1 && wave->counter > (wave->phase + wave->duty)){
      wave->state = 2;
    }
    else if (wave->state==2 && wave->counter> wave->period-1){
       wave->state = 0;
       wave->counter = 0;
    }
    wave->counter++;

    if (wave->state==1) {
      if (wave->polarity){waveMask |= powers[w];}
      else {waveMask &= wave_const - powers[w];}
    } else {
      if (wave->polarity){waveMask &= wave_const - powers[w];}
      else {waveMask |= powers[w];}
    }
  }
//DELAY is here now
  bool ontime = false;
  if((micros()-delayStart)<=DELAY_TIME) ontime=true;
  while ((micros() - delayStart) <= DELAY_TIME) { 
  }
  if(ontime) PORTG |= B00000010;
  else {
    digitalWrite(40,LOW);  
//    Serial.println("Warning: Clock not on time! ");
  }

  delayStart += DELAY_TIME; // this prevents drift in the delays
  
  //add hearbeat pin. high-low-high low on every delay time. 
  //status pin as probe on ontime to makesure that delaytime is taking the right amount of time. 

  unsigned long bitMask = (1<<8) - 1;
  PORTC = waveMask & bitMask; // last 8 bits
  PORTL = (waveMask&(bitMask << 8)) >> 8; // next 8 bits

  PORTG = (PORTG / 2) * 2 + !(PORTG % 2);
  int fISum = LOW;
}
