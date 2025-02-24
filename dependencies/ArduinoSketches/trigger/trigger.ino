#include <ArduinoJson.h>
#include "incbin.h"

// using incbin: https://github.com/AlexIII/incbin-arduino
INCTXT(ConfigFile, "trigger_config.json");

bool delayRunning = false; // true if still waiting for delay to finish

unsigned long DELAY_TIME = 100; // 10 us
unsigned long delayStart = 0; // the time the delay started
unsigned long prevTime = 0;
unsigned long led_gate = 0;
// counter increments each loop after trigger latch
unsigned long led_counter = 0; 
int led_gate_state = HIGH;

int fISum;
int latchState = LOW;
uint8_t trigFast, trigSlow; // save trig here
uint8_t fastMask=0, slowMask=0; // trig in mask for two ports

void setup(void) {
  Serial.begin(9600);

  // deserialize the json file text to a json object
  JsonDocument conf;
  DeserializationError error = deserializeJson(conf, gConfigFileData);
    if (error){
    Serial.println("Cannot load configuration file. Quitting.");
    return;
  }
  DELAY_TIME = conf["loop"];

  Serial.println("Trig\tEnabled\tName\tIn Pin\tFF Pin");
  for (JsonPair kv : conf.as<JsonObject>()) {
    const char* key = kv.key().c_str();
    int trig_num;
    if (sscanf(key, "trig%d", &trig_num) <=0) {
      continue; // continue if not wave#
    }
    trig_num -= 1; // change to 0 based
    JsonObject v = kv.value().as<JsonObject>();
    if (trig_num<8 && trig_num>=0) {
      fastMask += v["enabled"].as<bool>() << trig_num;
    } else if (trig_num>=8 && trig_num<16){
      slowMask += v["enabled"].as<bool>() << (trig_num-8);
    } else {
      Serial.println("Trigger position out of range! Quitting.");
    }
    Serial.print(trig_num); Serial.print("\t");
    v["enabled"] ? Serial.print("yes\t") : Serial.print("no\t");
    Serial.print(v["name"].as<const char*>()); Serial.print("\t");
    Serial.print(v["in"].as<int>()); Serial.print("\t");
    Serial.print(v["first_fault"].as<int>()); Serial.print("\n");
  }

  DDRA = B00000000; // Fan IN PINs 22-29
  DDRC = B00000000; // Fan IN PINs 37-30
  //Port Orientation may be flipped--Double check when connected!
  DDRE = B11111111; // Fan OUT PINs 0-1, 5, 2-3 (in that order)
  DDRH = B11111111; // Fan OUT PINs 17-16, 6-9 (in that order)
  DDRJ = B11111111; // Fan OUT PINs 15-14 (in that order)
  // Obligatory Spacer
  DDRB = B11111111; // Grudge PINs 53-50, 10-13
  DDRL = B11111111; // Grudge PINs 49-42
  // Obligatory Spacer
  pinMode(38, INPUT); // PIN IN for Trig Reset
  for(int a=39;a<42;) pinMode(a++, OUTPUT); // PIN OUT for Trig OR, ON-Time, Heartbeat

  // if led_gate==0, PD0 is always high
  // if led_gate>=, PD0 will be high for led_gate loops after trigger, then low
  led_gate = conf["led_gate"];

  if(led_gate==0) {
    PORTD |= B00000001; // PD0 set to high
    led_gate_state = HIGH;
  } else {
    PORTD &= B11111110; // PD0 set to low
    led_gate_state = LOW;
  }

  delayStart = micros(); // Start Delay
  delayRunning = true; // not finished yet

}

void loop(void) {
  //DELAY is here now
  bool ontime = false;
  if((micros()-delayStart)<=DELAY_TIME) ontime=true;
  while ((micros() - delayStart) <= DELAY_TIME) { 
  }
  if(ontime) PORTG |= B00000010;
  else PORTG &= B11111101;  

  delayStart += DELAY_TIME; // this prevents drift in the delays
  //add hearbeat pin. high-low-high low on every delay time. 
  //status pin as probe on ontime to makesure that delaytime is taking the right amount of time.

  //Heartbeat
  PORTG = (PORTG / 2) * 2 + !(PORTG % 2);

  int fISum = LOW;

  // set PD0 to low if led_gate is not 0, and counter>led_gate
  if(led_gate > 0) {
    if(led_gate_state) {
      if(led_counter >= led_gate) {
        PORTD &= B11111110; // PD0 set to low
        led_gate_state = LOW;
      }
      led_counter++; // increment counter
    }
  }

  //OR Gate for the Fan IN
  trigFast = PINA & fastMask;
  trigSlow = PINC & slowMask;
  if(trigSlow + trigFast) {
    if(latchState == LOW) {
      PORTB = trigFast;
      PORTL = trigSlow;
    }
    latchState = HIGH;
    fISum = HIGH;
    PORTE = B11111111;
    PORTH = B11111111;
    PORTJ = B11111111;
    Serial.print("FF B:\t"); Serial.print(trigSlow);
    Serial.print("\tFF L:\t"); Serial.println(trigFast);

    // set led_gate counter to 0 and PD0 to high
    if(led_gate>0){
      led_counter = 0;
      PORTD |= B00000001; // PD0 set to high
      led_gate_state = HIGH;
    }
  }


  //Trigger Reset
  if(PIND > 127 && latchState == HIGH){
    latchState = LOW;
    PORTE = B00000000;
    PORTH = B00000000;
    PORTJ = B00000000;
    PORTB = B00000000;
    PORTL = B00000000;
    Serial.println("Trigger reset.");
    
    if(led_gate>0){
      PORTD &= B11111110; // PD0 set to low
      led_gate_state = LOW;
    }
  }


  //Trig OR (Unlatched)
  //digitalWrite(39, fISum);
  if(fISum == HIGH){
    PORTG |= B00000100;
  }
  else {
    PORTG &= B11111011;
  }

  //Fast Compress Signal
  if(PINB> 0){
    PORTG |= B00100000;
  }
  else {
    PORTG &= B11011111;
  }

}
