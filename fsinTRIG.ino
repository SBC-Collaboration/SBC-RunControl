bool delayRunning = false; // true if still waiting for delay to finish

unsigned long DELAY_TIME = 100; // 10 us
unsigned long delayStart = 0; // the time the delay started
unsigned long prevTime = 0;

int fISum;
int latchState = LOW;


void setup (void) {
  //Serial.begin(9600);
  
//  for(int a=18;a<34;) pinMode(a++,INPUT); // PIN IN for Trig in
//  for(int a=34;a<50;) pinMode(a++, OUTPUT); // PIN OUT for Trig latch
  DDRA = B00000000; // Fan IN PINs 22-29
  DDRC = B00000000; // Fan IN PINs 37-30
  DDRB = B11111111; // Fan OUT PINs 53-50, 10-13
  DDRL = B11111111; // Fan OUT PINs 49-42
  pinMode(38, INPUT); // PIN IN for Trig reset
  for(int a=39;a<42;) pinMode(a++,OUTPUT); // PIN OUT for Trig OR, ON-Time, Heartbeat
  
  delayStart = micros(); //start delay
  delayRunning = true; // not finished yet

} 


void loop (void) {


  //DELAY is here now
  bool ontime = false;
  if((micros()-delayStart)<=DELAY_TIME) ontime=true;
  while ((micros() - delayStart) <= DELAY_TIME) { 
  }
  if(ontime) PORTG |= B00000010;
  else digitalWrite(40,LOW);  

  delayStart += DELAY_TIME; // this prevents drift in the delays
  //add hearbeat pin. high-low-high low on every delay time. 
  //status pin as probe on ontime to makesure that delaytime is taking the right amount of time. 
  //update_wave(&wave1);


  //Heartbeat
  PORTG = (PORTG / 2) * 2 + !(PORTG % 2);
  
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
