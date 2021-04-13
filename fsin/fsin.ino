/* Prof Dahl laid out an I/O map
 * <- 0-15 SQ Waves
 * -> 16-31 (not 13) Trig in
 * <- 33-47 Trig latch
 * -> 48 Trig reset
 * <- 49 Trig OR (unlatched)
 * <- 50 ON-Time status bit
 * <- 51 Heartbeat SQ wave?
 */

typedef struct square_wave {
    unsigned long period;
    unsigned long phase;
    unsigned long duty;
    bool polarity;
    int counter; //this is what Dr. Dahl called 'clock'
    int pin;
    int state;
   } Square_Wave;

bool delayRunning = false; // true if still waiting for delay to finish
Square_Wave wave1; 
unsigned long DELAY_TIME = 100; // 10 us
unsigned long delayStart = 0; // the time the delay started

void setup (void) {
  for(int a=0;a<16;) pinMode(a++,OUTPUT); // PIN OUT for SQ waves
  for(int a=16;a<32;) pinMode(a++,INPUT); // PIN IN for Trig in
  for(int a=32;a<47;) pinMode(a++, OUTPUT); // PIN OUT for Trig latch
  pinMode(48, INPUT); // PIN IN for the unlatched Trig reset
  for(int a=49;a<52;) pinMode(a++,INPUT); // PIN OUT for Trig OR, ON-Time, Heartbeat
  
  wave1.period = 10; //this should be going 100fps
  wave1.phase = 10;
  wave1.duty = 10;
  wave1.polarity = true;
  wave1.counter = 0;
  wave1.pin = 37;
  wave1.state = 0;
  pinMode(wave1.pin, OUTPUT);
  digitalWrite(wave1.pin, LOW); 
  delayStart = micros(); //start delay
  delayRunning = true; // not finished yet
  //unsigned long period;
  //unsigned long phase;
  //unsigned long duty;
  //byte polarity;
  //int counter; //this is what Dr. Dahl called 'clock'
  //int pin;
  //int state;
} 

void loop (void) {
  Square_Wave* wave = &wave1;
  bool ontime = false;
  while ((micros() - delayStart) <= DELAY_TIME) { 
    ontime = true;
  }
  delayStart += DELAY_TIME; // this prevents drift in the delays
  //add hearbeat pin. high-low-high low on every delay time. 
  //status pin as probe on ontime to makesure that delaytime is taking the right amount of time. 
  //update_wave(&wave1);
  if (wave->state==0 && wave->counter > wave->phase){
    wave->state = 1;
  }
  else if (wave->state==1 && wave->counter > (wave->phase + wave->duty)){
    wave->state = 2;
  }
  else if (wave->state==2 && wave->counter > wave->period){
     wave->state = 0;
     wave->counter = 0;
  }

  wave->counter++;

  if (wave->state==1) {
    if (wave->polarity){
      digitalWrite(wave->pin,HIGH); 
    }
    else
    {
      digitalWrite(wave->pin, LOW); 
    }
  }
  else 
  {
     if (wave->polarity){
      digitalWrite(wave->pin,LOW); 
    }
    else
    {
      digitalWrite(wave->pin, HIGH); 
    }
  }
} 
