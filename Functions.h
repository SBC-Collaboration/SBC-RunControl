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
