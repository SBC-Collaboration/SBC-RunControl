# Arduino-TriggerFIFO
Handles the trigger communication between different elements of SBC

# SQUARE WAVE CODE #
The following pinouts are from assigning the squarewaves to PORTH
Assigning more squarewaves to other ports should work just the same,
but the order of pins in each port should be double-checked when plugged in just to be sure.

In order, the square waves are assigned to the following pins in PORTH:
squarewave1 -- pin17
squarewave2 -- pin16
squarewave3 -- pin6
squarewave4 -- pin7
squarewave5 -- pin8
squarewave6 -- pin9
squarewave7 -- pin5
squarewave8 -- pin2
squarewave9 -- pin3

(the order is peculiar, yes, but I was not the one who designed the order of pins for PORTH)


# TRIG CODE #

the Pinout for the Trig code is separated into three categories: Fan-In, Fan-Out, and First Fault (or Grudge) Pins
Setting any pin in the Fan-In ports to HIGH will set all pins in the Fan-Out ports to HIGH until reset using Pin 38, aptly named the Trig Reset
Each pin in the Fan-In ports also corresponds to a First-Fault Pin, PORTA -- PORTB, PORTC -- PORTL. The order of pins within each port may be
reversed depending on the board used, so it would be a good idea to confirm the order of pins in these ports.


