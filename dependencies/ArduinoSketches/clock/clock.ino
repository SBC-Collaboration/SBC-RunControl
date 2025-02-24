#include <ArduinoJson.h>
#include "incbin.h"

// using incbin: https://github.com/AlexIII/incbin-arduino
INCTXT(ConfigFile, "clock_config.json");

typedef struct square_wave {
    bool enabled; // whether this wave is enabled
    int period; // x 100us = period (s)  
    int phase; // x 100us = offset for turning on
    int duty; // x 100us = time of being high
    bool polarity; // start high or low
    bool gated; // whether this channel is controlled by LED gate from trigger INO
    int counter=0; //this is what Dr. Dahl called 'clock'
    int state=0; // internal variable for whether it is currently high or low
   } Square_Wave;
Square_Wave waves[16];

bool delayRunning = false; // true if still waiting for delay to finish
int DELAY_TIME = 100; // 100 us
unsigned long delayStart = 0; // the time the delay started

unsigned long powers[16];
unsigned long waveMask = 0; // which pins should be high
bool led_gate;
unsigned long gate_mask = 0;

void setup(void) {
  Serial.begin(9600);
  while (!Serial) continue;

  // powers of 2, using bit shifting
  unsigned long base = 0b1;
  for (int i=0; i<16; i++) {powers[i] = base<<i;}
  
  // rail C and L set to output
  DDRC = B11111111; // digital pin 37-30
  DDRL = B11111111;  // digital pin 49-42
  // set pin 22 as input (LED gate)
  DDRA &= ~(1 << DDA0); // PA0

  // deserialize the json file text to a json object
  JsonDocument conf;
  DeserializationError error = deserializeJson(conf, gConfigFileData);

  if (error){
    Serial.println(F("Failed to read file"));
    Serial.println(error.c_str());
    return;
  }

  DELAY_TIME = conf["loop"];
  // extract from json object to square_wave class
  Serial.println("Wave\tEnabled\tGated\tPeriod\tPhase\tDuty\tPolarity");
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
    waves[wave_num].phase = v["phase"].as<int>() * waves[wave_num].period / 100;  // convert percentage to time
    waves[wave_num].duty = v["duty"].as<int>() * waves[wave_num].period / 100;  // convert percentage to time
    waves[wave_num].polarity = v["polarity"].as<bool>();
    waves[wave_num].gated = v["gated"].as<bool>();
    // convert wave gate to mask
    if(waves[wave_num].gated){
      gate_mask |= (1<<wave_num);
    } else {
      gate_mask &= ~(1<<wave_num);
    }

    Serial.print(wave_num); Serial.print("\t");
    waves[wave_num].enabled ? Serial.print("yes\t") : Serial.print("no\t");
    waves[wave_num].gated ? Serial.print("yes\t") : Serial.print("no\t");
    Serial.print(waves[wave_num].period); Serial.print("\t");
    Serial.print(waves[wave_num].phase); Serial.print("\t");
    Serial.print(waves[wave_num].duty); Serial.print("\t");
    Serial.print(waves[wave_num].polarity); Serial.print("\n");
  }
  delayStart = micros();
}

void loop(void) {  
  // get LED gate status from trigger arduino
  led_gate = (PINA & (1 << PINA0)) != 0;
  // wave states: 0: before HIGH, 1: HIGH, 2: After HIGH
  Square_Wave* wave;
  //Waves:
  for(int w=0; w<16; w++){
    wave = &waves[w];
    wave->counter++;
    if (wave->enabled < 1) {
      continue; // skip if not enabled
    }
    if (wave->state==0 && wave->counter > wave->phase){
      wave->state = 1;
      // when changing from low to high, change wavemask
      // high if polarity is true, and low if not
      if (wave->polarity) {
        waveMask |= powers[w];
      } else {
        waveMask &= ~powers[w];
      }
    }
    else if (wave->state==1 && wave->counter > (wave->phase + wave->duty)){
      wave->state = 2;
      // when changing from high to low, change wavemask
      // low if polarity is true, and low if not
      if (wave->polarity) {
        waveMask &= ~powers[w];
      } else {
        waveMask |= powers[w];
      }
    }
    else if (wave->state==2 && wave->counter >= wave->period){
       wave->state = 0;
       wave->counter = 0;
    } else {
      continue; // skip if not changed
    }
  }

  if(!led_gate){
    // turn gated pins off if LED gate pin is low
    waveMask &= ~gate_mask;
  }

//DELAY is here now
  bool ontime = false;
  long time = micros()-delayStart;

  if(time <= DELAY_TIME) {
    PORTG |= B00000010;
    delayStart += DELAY_TIME; // change delay start to next loop's value
    while (micros() < delayStart) { } // wait for delay time to pass 
  }
  else {
    PORTG &= B11111101;
    Serial.print("Warning: Clock not on time! "); Serial.println(time);
    delayStart = micros();
  }

  PORTC = waveMask & B11111111; // last 8 bits
  PORTL = (waveMask >> 8) & B11111111; // next 8 bits

  // toggle PG0 for heartbeat
  // but this line along seems to take 20+us
  // PORTG ^= B00000001;
  // and this line works fine...
  PORTG = (PORTG / 2) * 2 + !(PORTG % 2);
}