// ARDUINO UTI Shield Readout
// S. Luitz @ SLAC 2016

// the board
//
// Notes:
//
// sel1 and sel4 are permanently hardwired to "0" - this allows us to program the following modes:
// sel2 = 0, sel3 = 0 : 5 caps 0-2pF
// sel2 = 0, sel3 = 1 : 5 caps 0-12pF
// sel2 = 1, sel3 = 0 : 3 caps, variable range 0-300pf
// sel2 = 1, sel3 = 1 : unused (Thermistor 1-25kOhm, 4-wire)
//



#include <SPI.h>
#include <Ethernet.h>
#include <EEPROM.h>
#include "MgsModbus.h"




#define EEPROM_BASE_NET 0
#define EEPROM_BASE_CONF 40

#define CKSUM_INIT 0xaa

// Ethernet settings

byte mac[6] = {0xa8,0x61,0x0a,0xae,0x87,0x43 };
char macstr[18];
IPAddress ip(192,168,137,150);
IPAddress gateway(192,168,137,1);
IPAddress subnet(255,255,255,0);
IPAddress nameserver(192,168,137,1);

#define DEBUG
#define DEBUG1



// mode (use micros() to obtain time vs loop count)

 // #define MICROS 

// board connections
const uint8_t  NCHIPS = 2;    // number of chips on the board

// chips are numbered:
// ---------
// ! 3 4 5 !
// ! 0 1 2 !
// ---------

// output pin of chip 0 relocated from 4 to 11 (4 is actually reserved by the Ethernet shield)
// output in of chip 3 relocated from 50 to 34 (50 is also used by Ethernet Shield)
// to be fixed in next revision of board


//const uint8_t  out[NCHIPS] = { 11, 44, 7, 34, 26, 32 };  
//const uint8_t  sel2[NCHIPS] = {2, 42, 5, 24, 48, 30 };  
//const uint8_t  sel3[NCHIPS] = {3, 40, 6, 22, 46,  28 };  


//const uint8_t  out[NCHIPS]  = { 11, 44, 34,  7,  26, 32 };  
//const uint8_t  sel2[NCHIPS] = {  2, 42, 48,  5,  24, 30 };  
//const uint8_t  sel3[NCHIPS] = {  3, 40, 46,  6,  22, 28 };  

// for only two chips
const uint8_t  out[NCHIPS]  = { 11, 7 };
const uint8_t  sel2[NCHIPS] = {  2, 5 };  
const uint8_t  sel3[NCHIPS] = {  3, 6 };  

// Can possibly set NCHIPS = 1; for different configurations

//const uint8_t  out[NCHIPS] = { 4, x 50 };
//const uint8_t  sel2[NCHIPS] = { 2 x 48 };
//const uint8_t  sel3[NCHIPS] = { 3 x 46 };
// UTI readout modes

const uint8_t  MODE_off = 0;
const uint8_t  MODE_2pf = 1;
const uint8_t  MODE_12pf = 2;
const uint8_t  MODE_300pf = 3;

// other constants

const uint8_t MAXPHASES = 5;
const unsigned long MAXWIDTH = 200000;

// Default Mode & Multiplier
#define DEFMODE MODE_300pf
#define DEFMULT 6000

const float tol = 1.3;


// Modbus configuration

// modbus registers

// for each chip:
// 0: mode (0: off, 1: 2pf, 2: 12pf, 3: 300pf) -- default is 2
// 1: status 
// 2+3 : 32-bit unsigned ratio 1 * 1E6
// 4+5 : 32-bit unsigned ratio 2 * 1E6 (only modes 1 and 2)
// 6+7 : 32-bit unsigned ration 3 * 1E6 (only modes 1 and 2)


// 



// 1: multiplier (sets 10% output at C_meas = C_ref) 
//    default is 6000 - corresponding to a reading of 60000 for C_meas = C_ref
// 2: valid (>0: OK, 0: error)s
// 3: Offset-corrected ratio for D/C
// 4: Offset-corrected ratio for E/C (0 in mode 3)
// 5: Offset-corrected ratio for F/C (0 in mode 3)

const int MBOFF_MODE = 0;
const int MBOFF_STATUS = 1;
const int MBOFF_DATA = 2; // start of data area



const int NREGS = 1+1+3*2;  // number of 16-bit Modbus registers per chip
const int MBDATALEN = NREGS * NCHIPS;

word mbdata[MBDATALEN];    // the modbus data
MgsModbus Mb(MBDATALEN, mbdata);

const word STATUS_OK = 0x01;        // we have a value
const word STATUS_CLIPPED_LOW = 0x02;   // result was clipped to zero
const word STATUS_DIVZERO = 0x04; // division by zero in the ratio calculation 



uint8_t ledblink = 0;


void setup() {

uint8_t i;
  
// put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Serial initialized");

  #ifdef MICROS
    Serial.println("Using micros() to measure time");
  #endif
  
  // initialize input and output pins
  for(i=0; i< NCHIPS; i++) {
    if (sel2[i]) pinMode(sel2[i],OUTPUT);
    if (sel3[i]) pinMode(sel3[i],OUTPUT);
    if (out[i])  pinMode(out[i],INPUT);
  }
  

  // set pin 13 so that we can blink the LED
  
  pinMode(13,OUTPUT);

// set up network
#ifdef MACADDR
// on first run generate MAC address and store in EEPROM
 
  if (EEPROM.read(1) == '&') {
    for (int i = 2; i < 6; i++) {
      mac[i] = EEPROM.read(i);
    }
  } else {
    int seed = 0;
    for (int j=0; j<50; j++)
       for (int i=0; i<NCHIPS; i++) {
          seed+=digitalRead(out[i]); seed +=analogRead(0);
          delay(10); 
       }       
    randomSeed(seed);
    for (int i = 2; i < 6; i++) {
      mac[i] = random(0, 255);
      EEPROM.write(i, mac[i]);
    }
    EEPROM.write(1, '#');
  }
  snprintf(macstr, 18, "%02x:%02x:%02x:%02x:%02x:%02x", mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
  Serial.println(macstr);
  #endif

  // Try DHCP

  Serial.println("Attempting to get IP configuration through DHCP");
  snprintf(macstr, 18, "%02x:%02x:%02x:%02x:%02x:%02x", mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
  Serial.print("MAC address: "); Serial.println(macstr);

//  if (Ethernet.begin(mac,10000,10000)) {
//     // Success - this is our new config
//     Serial.println("DHCP Success!");     
//  }
//
//  else  {
//      Serial.println("DHCP Failure! Using default IP address");
//      Ethernet.begin(mac, ip, nameserver, gateway, subnet);   // start ethernet interface
//  }
 Serial.println("Using default IP address");
 Ethernet.begin(mac, ip, nameserver, gateway, subnet);
 Serial.println("Ethernet interface started"); 
 Serial.print("IP Address: "); Serial.println(Ethernet.localIP());
 Serial.print("Netmask: "); Serial.println(Ethernet.subnetMask());
 Serial.print("Gateway: "); Serial.println(Ethernet.gatewayIP());


  // Initialize MbData
  for (i=0; i< MBDATALEN; i++) Mb.MbData[i] = 0;

  if(EEPROM_read_conf() == 0) {
    // use default if we can't read from EEPROM
     for (i=0; i< NCHIPS; i++) {
      int mbo = i * NREGS;
      Mb.MbData[mbo+MBOFF_MODE] = DEFMODE;
    }
}

}




void loop() {
  // put your main code here, to run repeatedly:

unsigned long counts[MAXPHASES];
unsigned long ref; // reference measurement 
uint8_t phases;
int i,j; 
int mbo;
int nval;
float offset; // offset measurement
float ratio[3];   // D/C, E/C, F/C

    // loop over all chips
    for(i=0; i<NCHIPS; i++) { //NCHIPS
      mbo = i*NREGS;
      
      for (j=MBOFF_STATUS; j<NREGS; j++) Mb.MbData[mbo+j] = 0; // clear data and data valid flag, leave mode and multiplier alone
       if (Mb.MbData[mbo+MBOFF_MODE] > 0) {
         // set set UTI mode and read the result
         setUTIMode(i,Mb.MbData[mbo+MBOFF_MODE] & 0x03);
         delay(50);
         ReadUTI(i,&phases,counts);   
     
     
      #ifdef DEBUG
          Serial.println("+++++++++++++++++++++++++++++++++++");
          Serial.print("Chip: "); Serial.println(i);
          Serial.print("Mode: "); Serial.println(Mb.MbData[mbo+MBOFF_MODE]);
          //Serial.print("FR: "); Serial.println(Mb.MbData[mbo+MBOFF_MULT]);
          Serial.print("Phases detected: "); Serial.println(phases);
      #endif

     
      if (! phases) {  
         continue;    // readout error .. try next chip
      }
      
       offset = counts[0];
       ref = counts[1];

       #ifdef DEBUG1
       Serial.print("Offset: "); Serial.println(offset);
       Serial.println("Counts: ");
       for (int k=0; k< phases; k++) {
         Serial.print(k); Serial.print(":");Serial.println(counts[k]);
       }
       #endif
        
    
      if (Mb.MbData[mbo+MBOFF_MODE] == 3) {
         // this is mode 3 - we expect a 3-phase cycle
         if (phases != 3) {
           Serial.print("************ Wrong number of phases in 3-phase cycle ****");
           continue;
         }

         nval = 1; // we measured one value
      }
      else {
      // modes 1 or 2 are 5-phase cycles
         if (phases != 5) {
           Serial.print("************ Wrong number of phases in 5-phase cycle ****"); 
           continue;
         } 
         nval = 3; // we measured 3 values   
      }
      
      // calculate ratios and apply full-range calibration
      for (int v = 0; v < nval; v++) {

        if (ref != offset) {   // make sure to not divide by 0
           ratio[v] = (counts[2+v]-offset)/(ref-offset);        
        }
        else {
           ratio[v] = 0; 
           Mb.MbData[mbo+MBOFF_STATUS] |= STATUS_DIVZERO;         
        }
        if (ratio[v] < 0) { // clamp lower limit of ratio to 0 
          ratio[v] = 0;
          Mb.MbData[mbo+MBOFF_STATUS] |= STATUS_CLIPPED_LOW;
        }

        float r = ratio[v];
        //Serial.println(r);

        

        enc_float(&Mb.MbData[mbo+MBOFF_DATA+2*v],r);
        Serial.print("Addr: "); Serial.print(mbo+MBOFF_DATA+2*v); Serial.print(" Value: "); Serial.println(r);
       
      

//        if (r <= 65535) {
//          Mb.MbData[mbo+MBOFF_DATA+v] = r;
//        }
//        else {
//          Mb.MbData[mbo+MBOFF_DATA+v] = 65535;
//          Mb.MbData[mbo+MBOFF_STATUS] |= STATUS_CLIPPED_HIGH;
//        }


        Mb.MbData[mbo+MBOFF_STATUS] |= STATUS_OK;

        

        
        #ifdef DEBUG
          Serial.print("Ratio "); Serial.print(v); Serial.print(" = "); Serial.println(ratio[v],5);
        #endif

        

        
        

        
        
      }

    }
    // give the system a better chance to respond to network requests by looping over MbsRun
       
    for (int n=0; n< 5; n++) {
     Mb.MbsRun();  // talk TCP here
     delay(30);
     ledblink  = (ledblink ? 0 : 1);
     if (ledblink) digitalWrite(13,1); else digitalWrite(13,0);
  }
     

   // blink LED
    ledblink  = (ledblink ? 0 : 1);
    if (ledblink) digitalWrite(13,1); else digitalWrite(13,0);
   
 } // loop over CHIPS

 EEPROM_write_conf(); 

}


void setUTIMode(uint8_t chip, uint8_t mode) {

// sel2 = 0, sel3 = 0 : 5 caps 0-2pF
// sel2 = 0, sel3 = 1 : 5 caps 0-12pF
// sel2 = 1, sel3 = 0 : 3 caps, variable range 0-300pf

  //mode = 2;
  
  switch (mode) {
    
     case MODE_2pf :
       digitalWrite(sel2[chip],0);
       digitalWrite(sel3[chip],0);
       break;

     case MODE_12pf :
       digitalWrite(sel2[chip],0);
       digitalWrite(sel3[chip],1);
       break;

     case MODE_300pf :
       digitalWrite(sel2[chip],1);
       digitalWrite(sel3[chip],0);
     break;
    
  }
}


int ReadUTI(uint8_t chip, uint8_t *phases, unsigned long counts[])
{
   const int ncyc = 15; 
   unsigned long width[ncyc];
   uint8_t index[ncyc];
   uint8_t startindex;
   uint8_t ph;
   int state = HIGH;
   uint8_t i;
   unsigned long width_low, width_high;

   #ifdef MICROS
   unsigned long t0, t1;
   #endif

   uint8_t pin = out[chip];

  

   uint8_t bit = digitalPinToBitMask(pin);
   uint8_t port = digitalPinToPort(pin);
   uint8_t stateMask = (state ? bit : 0);

   for (i=0; i<ncyc; i++) { 
      width[i]=0;
      index[i]=i;
   }

   // measure pulse lengths - Make sure we don't block forever

   #ifndef MICROS
   noInterrupts();   // turn off interrupts to get more preceise timing measurements
   #endif

   width_low = MAXWIDTH;
   while (((*portInputRegister(port) & bit) != stateMask) && width_low > 0) width_low--; // wait for input to go HIGH

   if (width_low == 0) {    
       // we did not find the expected edge
      #ifdef DEBUG
        Serial.println("Error: Timeout while waiting for initial edge");
      #endif
        #ifndef MICROS
         interrupts();
        #endif
        *phases =0;
        return -1;
   }
  
   for (i=0; i<ncyc; i++) {
     width_low = MAXWIDTH;
     width_high=MAXWIDTH;
     #ifdef MICROS
     t0 = micros();
     #endif
     while (((*portInputRegister(port) & bit) == stateMask) && width_high > 0) width_high--;  //Count the HIGH time 
     while (((*portInputRegister(port) & bit) != stateMask) && width_low > 0) width_low--;  //Count the LOW time
     #ifdef MICROS
     t1 = micros();
     #endif
     if ((width_high == 0) || width_low == 0) {
        // we did not find the expected edge
        #ifdef DEBUG
        Serial.println("Error: Timeout while waiting for edge");
        #endif
        #ifndef MICROS
        interrupts();
        #endif
        *phases = 0;
        return -1;     
     }  
     

     #ifdef MICROS
       width[i]=t1-t0;
     #else
       width[i]=2*MAXWIDTH - (width_low+width_high);
     #endif
   }

   #ifndef MICROS
   interrupts();
   #endif


   // find start of train assuming a 3-phase pulse train

   ph = 3;
   startindex = 0;
   
   for (i=1; i<ncyc-6; i++) {
     if (  abs((long) width[i]- (long) width[i+1]) < 100 && 
           width[i]*tol<width[i+2] && width[i]*tol<width[i+3] 
            && width[i+1]*tol < width[i+2] && width[i+1]*tol < width[i+3]) {
        startindex = i;
        break;
     }
   }

   if (startindex == 0) {
     // we didn't find a start index. Set phases to 0 and return error.
     
     #ifdef DEBUG
     Serial.println("Error: Could not find startindex");
     #endif
   *phases = 0;
   return -1;  
   }
    
    // check for 4 and 5 phases
    if (width[startindex+4] > tol*width[startindex]) ph = 4;
    if (width[startindex+5] > tol*width[startindex]) ph = 5;



    #ifdef DEBUG1
    Serial.println("****************************");
    Serial.print("Chip: "); Serial.println(chip); 
    Serial.print("Startindex: "); Serial.println(startindex);
    Serial.print("Phases: "); Serial.println(ph);
    Serial.println("-----");
    for (i=startindex; i<=startindex+ph; i++) {
      Serial.print(i); Serial.print(": "); Serial.println(width[i]);
    }
    #endif   

    // copy counts & # of phases
    counts[0]=width[startindex]+width[startindex+1];  // offset count is sum of first two widths
    for (i=1; i<ph; i++) counts[i] = width[startindex+i+1]; 
    *phases = ph;

     return 0;
}


// only write values that are different
// #define EEPROM_cond_write(addr,val)    if( (EEPROM.read((addr)) != (val))) EEPROM.write((addr),(val) ) 

void EEPROM_cond_write(int addr, byte val) 

{ 
  if( (EEPROM.read((addr)) != (val))) {
    EEPROM.write(addr,val); 
    #ifdef DEBUG
      Serial.print("WRITE_COND"); Serial.print(addr); Serial.print(":"); Serial.println(val);
    #endif
  }
}


   
void EEPROM_write_conf (){

int addr = EEPROM_BASE_CONF;
uint8_t cksum = CKSUM_INIT;
uint8_t val;


#ifdef DEBUG
  Serial.println("Updating EEPROM configuration");
#endif
for (int i=0; i<NCHIPS; i++) {
  int mbo = i * NREGS;
  val = Mb.MbData[mbo+MBOFF_MODE] & 0xff;
  EEPROM_cond_write(addr+i,val);
  cksum ^= val;
}

// write checksum
  EEPROM_cond_write(addr+NCHIPS, cksum);
}
  


int EEPROM_read_conf() {
  
uint8_t cksum = CKSUM_INIT;
int addr = EEPROM_BASE_CONF;

#ifdef DEBUG
  Serial.println("Reading EEPROM configuration");
#endif

// verify checksum
for (int i=0; i< NCHIPS; i++) 
  cksum ^= EEPROM.read(addr+i);

if (cksum == EEPROM.read(addr+NCHIPS)) {
  // checksum OK, read values
  #ifdef DEBUG
  Serial.println("EEPROM: Checksum OK");
  #endif
  for (int i=0; i< NCHIPS; i++) {
    int mbo = i*NREGS;
    Mb.MbData[mbo+MBOFF_MODE] = EEPROM.read(addr+i);
  }
  return 1;
}   
else {
   // checksum not OK
   #ifdef DEBUG
   Serial.println("EEPROM: Checksum NOT OK");
   #endif
   return 0;
}

}

void enc_float(word *t, float x) {


  union U {float f; uint32_t u;};
  union U u;
  u.f = x;
  t[0] = (u.u >> 16) & 0xffffU;
  t[1] = (u.u & 0xffffU) ;


}




 
