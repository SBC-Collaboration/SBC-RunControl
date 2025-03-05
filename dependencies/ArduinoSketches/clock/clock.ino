#include <ArduinoJson.h>
#include "incbin.h"

// using incbin: https://github.com/AlexIII/incbin-arduino
INCTXT(ConfigFile, "clock_config.json");

// The integer data types need to be 16 bit to run fast enough
// If loop time is 100us, then that means maximum period is 65535*100us = 6.5535s
typedef struct square_wave {
    bool enabled; // whether this wave is enabled
    uint16_t period; // x 100us = period (s)  
    uint16_t  phase; // x 100us = offset for turning on
    uint16_t  duty; // x 100us = time of being high
    bool polarity; // start high or low
    bool gated; // whether this channel is controlled by LED gate from trigger INO
    uint16_t counter=0; //this is what Dr. Dahl called 'clock'
   } Square_Wave;
Square_Wave waves[16];

bool delayRunning = false; // true if still waiting for delay to finish
int DELAY_TIME; // time to wait between loops
unsigned long delayStart = 0; // the time the delay started

unsigned long powers[16];
uint16_t waveMask = 0; // which pins should be high
bool led_gate;
uint16_t gate_mask = 0;

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
    waves[wave_num].period = v["period"].as<uint16_t>();
    waves[wave_num].phase = v["phase"].as<uint32_t>() * waves[wave_num].period / 100;  // convert percentage to time
    waves[wave_num].duty = v["duty"].as<uint32_t>() * waves[wave_num].period / 100;  // convert percentage to time
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
    waves[wave_num].polarity ? Serial.print("true\t") : Serial.print("false\t");; Serial.print("\n");
  }
  delayStart = micros();
}

void loop(void) {
  // Read LED gate status from trigger arduino
  led_gate = (PINA & (1 << PINA0)) != 0;

  waveMask = 0;
  
  for (int w = 0; w < 16; w++) {
    Square_Wave* wave = &waves[w];
    if (!wave->enabled)
      continue;
    
    // Increment the counter and wrap it manually
    wave->counter++;
    if (wave->counter >= wave->period)
      wave->counter = 0;
    
    bool isHigh = false;
    
    // Check if the HIGH period wraps around the period end
    if (wave->phase + wave->duty <= wave->period) {
      // No wrap: simply check if the counter is within [phase, phase+duty)
      if (wave->counter >= wave->phase && wave->counter < wave->phase + wave->duty)
        isHigh = true;
    } else {
      // Wrapped case: calculate how much the duty goes past the period
      int wrap = wave->phase + wave->duty - wave->period;
      // HIGH if counter is after phase or before the wrap value
      if (wave->counter >= wave->phase || wave->counter < wrap)
        isHigh = true;
    }
    
    // Invert if polarity is false
    if (!wave->polarity)
      isHigh = !isHigh;
    
    // Build new mask based on the channel's state
    if (isHigh)
      waveMask |= powers[w];
  }
  
  // When LED gate is LOW, turn off gated channels.
  if (!led_gate)
    waveMask &= ~gate_mask;
  
  // Timing delay: wait until DELAY_TIME has elapsed
  unsigned long now = micros();
  if (now - delayStart < DELAY_TIME) {
    PORTG |= B00000010; // Set ontime pin
    delayStart += DELAY_TIME; // change delay start to next loop's value
    while (micros() < delayStart) { } // wait for delay time to pass 
  } else {
    // Print if it's not on time. Reset timer to start again
    Serial.print("Warning: Clock not on time! ");
    Serial.println(now - delayStart);
    delayStart = micros();
  }
  
  // Update outputs 
  PORTC = waveMask & 0xFF; // lower 8 bits
  PORTL = (waveMask >> 8) & 0xFF; // upper 8 bits
  
  // Toggle heartbeat on PORTG bit0 (optimized toggle)
  PORTG = (PORTG / 2) * 2 + !(PORTG % 2);
}
