bool delayRunning = false; // true if still waiting for delay to finish

unsigned long DELAY_TIME = 100; // 10 us
unsigned long delayStart = 0; // the time the delay started
unsigned long prevTime = 0;

int fISum;
int latchState = LOW;



void setup(void) {
  //Serial.begin(9600);

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

  //OR Gate for the Fan IN
  if(PINA + PINC > 0) {
    if(latchState == LOW) {
      PORTB = PINA;
      PORTL = PINC;
    }
    latchState = HIGH;
    fISum = HIGH;
    PORTE = B11111111;
    PORTH = B11111111;
    PORTJ = B11111111;
  }


  //Trigger Reset
  if(PIND > 127 && latchState == HIGH){
    latchState = LOW;
    PORTE = B00000000;
    PORTH = B00000000;
    PORTJ = B00000000;
    PORTB = B00000000;
    PORTL = B00000000;
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
