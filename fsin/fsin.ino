/* Prof Dahl laid out an I/O map
 * <- 2-17 SQ Waves
 * -> 18-33 Trig in
 * <- 34-49 Trig latch
 * -> 50 Trig reset
 * <- 51 Trig OR (unlatched)
 * <- 52 ON-Time status bit
 * <- 53 Heartbeat SQ wave?
 * 
 * IMPORTANT: PINs 20 and 21 must be plugged in, otherwise they read HIGH by default and that would not work.
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

int fISum;
int latchState = LOW;

void setup (void) {
  Serial.begin(9600);
  
  for(int a=2;a<18;) pinMode(a++,OUTPUT); // PIN OUT for SQ waves
  for(int a=18;a<34;) pinMode(a++,INPUT); // PIN IN for Trig in
  for(int a=34;a<50;) pinMode(a++, OUTPUT); // PIN OUT for Trig latch
  pinMode(50, INPUT); // PIN IN for Trig reset
  for(int a=51;a<54;) pinMode(a++,OUTPUT); // PIN OUT for Trig OR, ON-Time, Heartbeat
  
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

  //Or gate for the fan in
  fISum=0;
  for(int i=18; i<34;){
    fISum += digitalRead(i++);
  }
  if(fISum > 0) {
    latchState = HIGH;
    for(int i=34; i<50;){
      digitalWrite(i++, HIGH);
    }
  }
  //Trigger reset
  if(digitalRead(50) > 0){
    for(int i=34; i<50;){
      latchState = LOW;
      digitalWrite(i++, LOW);
    }
  }
  //Trig OR (unlatched)
  if(fISum>0) digitalWrite(51, HIGH);
  else digitalWrite(51, LOW);

  Serial.println(fISum);
} 
