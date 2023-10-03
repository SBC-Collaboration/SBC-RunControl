typedef struct square_wave {
    unsigned long period; // x 100us = period (s)  
    unsigned long phase; // x 100us = offset
    unsigned long duty; // x 100us = duration high
    bool polarity; // start high or low
    int counter; //this is what Dr. Dahl called 'clock'
    int pin; 
    int state; // internal variable for whether it is currently high or low
   } Square_Wave;
Square_Wave waves[16];


bool delayRunning = false; // true if still waiting for delay to finish
Square_Wave wave1; 
Square_Wave wave2;
Square_Wave wave3; 
Square_Wave wave4;
Square_Wave wave5;
Square_Wave wave6;
Square_Wave wave7;
Square_Wave wave8;
Square_Wave wave9;
unsigned long DELAY_TIME = 100; // 10 us
unsigned long delayStart = 0; // the time the delay started
unsigned long prevTime = 0;

int powers[] = {1,2, 8,16,32,64,128,256,512};
int waveNum = 0;


void setup (void) {
  //Serial.begin(9600);
  
  for(int a=2;a<18;) pinMode(a++,OUTPUT); // PIN OUT for SQ waves 
  
  //SQ Wave PINs in order: 17 16 6 7 8 9 5 2 3
  DDRH = B11111111; // PIN OUT for SQ waves
  
  wave1.period = 100; //this should be going 100fps
  wave1.phase = 0;
  wave1.duty = 10 ;
  wave1.polarity = true;
  wave1.counter = 0;
  wave1.pin = 2;
  wave1.state = 0;
  
  delayStart = micros(); //start delay
  delayRunning = true; // not finished yet

  wave2.period = 3; //this should be going 100fps
  wave2.phase = 0;
  wave2.duty = 1;
  wave2.polarity = true;
  wave2.counter = 0;
  wave2.pin = 3;
  wave2.state = 0;

  wave3.period = 20; //this should be going 100fps
  wave3.phase = 0;
  wave3.duty = 5;
  wave3.polarity = true;
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
  wave5.polarity = true;
  wave5.counter = 0;
  wave5.pin = 6;
  wave5.state = 0;
  wave5.period = 20; 

  wave6.period = 20; //this should be going 100fps
  wave6.phase = 0;
  wave6.duty = 5;
  wave6.polarity = false;
  wave6.counter = 0;
  wave6.pin = 6;
  wave6.state = 0;
  wave6.period = 20;
  
  wave7.period = 20; //this should be going 100fps
  wave7.phase = 0;
  wave7.duty = 5;
  wave7.polarity = true;
  wave7.counter = 0;
  wave7.pin = 6;
  wave7.state = 0;
  wave7.period = 20;

  wave8.period = 20; //this should be going 100fps
  wave8.phase = 0;
  wave8.duty = 5;
  wave8.polarity = false;
  wave8.counter = 0;
  wave8.pin = 6;
  wave8.state = 0;
  wave8.period = 20;
  
  wave9.period = 20; //this should be going 100fps
  wave9.phase = 0;
  wave9.duty = 5;
  wave9.polarity = true;
  wave9.counter = 0;
  wave9.pin = 6;
  wave9.state = 0;
  wave9.period = 20;
  
  waves[0] = wave1;
  waves[1] = wave2;
  waves[2] = wave3;
  waves[3] = wave4;
  waves[4] = wave5;
  waves[5] = wave6;
  waves[6] = wave7;
  waves[7] = wave8;
  waves[8] = wave9;
  Square_Wave* wave[16];
  //for(int i=0;i<15;i++) wave[i] = &waves[i];
} 


void loop (void) {
//  Square_Wave* wave = &wave1;

  
  

  
  //Waves:
  for(int w=0; w<9; w++){
    Square_Wave* wave = &waves[w];
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
      if (wave->polarity){
        //digitalWrite(wave->pin,HIGH); 
        waveNum |= powers[w];
      }
      else
      {
        //digitalWrite(wave->pin, LOW); 
        waveNum &= 511-powers[w];
      }
    }
    else 
    {
       if (wave->polarity){
        //digitalWrite(wave->pin,LOW);
        waveNum &= 511-powers[w];
      }
      else
      {
        //digitalWrite(wave->pin, HIGH); 
        waveNum |= powers[w];
      }
    }
  }

  //update_wave(&wave1);

  
  PORTH = waveNum % 128;
  PORTE = (waveNum/128) * 8;

} 
