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
Square_Wave waves[16];


bool delayRunning = false; // true if still waiting for delay to finish
Square_Wave wave1; 
Square_Wave wave2;
Square_Wave wave3; 
Square_Wave wave4;
Square_Wave wave5;
unsigned long DELAY_TIME = 100; // 10 us
unsigned long delayStart = 0; // the time the delay started
unsigned long prevTime = 0;

int fISum;
int latchState = LOW;

void setup (void) {
  //Serial.begin(9600);
  
  for(int a=2;a<18;) pinMode(a++,OUTPUT); // PIN OUT for SQ waves

  DDRB = B11111111; // PIN OUT for SQ waves
//  for(int a=18;a<34;) pinMode(a++,INPUT); // PIN IN for Trig in
//  for(int a=34;a<50;) pinMode(a++, OUTPUT); // PIN OUT for Trig latch
  DDRA = B00000000; // Fan IN PINs 22-29
  DDRC = B00000000; // Fan IN PINs 37-30
  DDRB = B11111111; // Fan OUT PINs 53-50, 10-13
  DDRL = B11111111; // Fan OUT PINs 49-42
  pinMode(38, INPUT); // PIN IN for Trig reset
  for(int a=39;a<42;) pinMode(a++,OUTPUT); // PIN OUT for Trig OR, ON-Time, Heartbeat
  
  wave1.period = 10; //this should be going 100fps
  wave1.phase = 0;
  wave1.duty = 5;
  wave1.polarity = true;
  wave1.counter = 0;
  wave1.pin = 2;
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

  wave2.period = 2; //this should be going 100fps
  wave2.phase = 0;
  wave2.duty = 1;
  wave2.polarity = true;
  wave2.counter = 0;
  wave2.pin = 3;
  wave2.state = 0;

  wave3.period = 20; //this should be going 100fps
  wave3.phase = 0;
  wave3.duty = 5;
  wave3.polarity = false;
  wave3.counter = 0;
  wave3.pin = 4;
  wave3.state = 0;

  wave4.period = 20; //this should be going 100fps
  wave4.phase = 0;
  wave4.duty = 5;
  wave4.polarity = false;
  wave4.counter = 0;
  wave4.pin = 5;
  wave4.state = 0;

  wave5.period = 20; //this should be going 100fps
  wave5.phase = 0;
  wave5.duty = 5;
  wave5.polarity = false;
  wave5.counter = 0;
  wave5.pin = 6;
  wave5.state = 0;
  wave5.period = 20; 
  
  waves[0] = wave1;
  waves[1] = wave2;
  waves[2] = wave3;
  waves[3] = wave4;
  waves[4] = wave5;
  Square_Wave* wave[16];
  //for(int i=0;i<15;i++) wave[i] = &waves[i];
} 

void loop (void) {
//  Square_Wave* wave = &wave1;
  bool ontime = false;
  while ((micros() - delayStart) <= DELAY_TIME) { 
    ontime = true;
  }
  if(ontime) PORTG |= B00000010;
  else digitalWrite(40,LOW);
  
  delayStart += DELAY_TIME; // this prevents drift in the delays
  //add hearbeat pin. high-low-high low on every delay time. 
  //status pin as probe on ontime to makesure that delaytime is taking the right amount of time. 
  //update_wave(&wave1);

  //Waves:
  for(int w=0; w<5; w++){
    Square_Wave* wave = &waves[w];
    if (wave->state==0 && wave->counter > wave->phase){
      wave->state = 1;
    }
    else if (wave->state==1 && wave->counter > (wave->phase + wave->duty)){
      wave->state = 2;
    }
    else if (wave->state==2 && wave->counter> wave->period){
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

  int fISum = LOW;
  
  //Or gate for the fan in
  if(PINA+PINC>0) {
    latchState = HIGH;
    fISum = HIGH;
    PORTB = B11111111;
    PORTL = B11111111;
  }

  
  //Trigger reset
  if(PIND > 127 && latchState == HIGH){
    latchState = LOW;
    PORTB = B00000000;
    PORTL = B00000000;
  }
  
  //Trig OR (unlatched)
  digitalWrite(39, fISum);
  if(fISum == HIGH){
    PORTG |= B00000100;
  }

} 
