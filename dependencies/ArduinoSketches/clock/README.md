# Arduino-GateGenerator
Generates the clock signal that control image acquisition and illumination for SBC.

The clock part of the code has been separated from the trigger part of the code by Ethan. See SBC-TriggerFIFO repository. It now has a working implementation of json that controls all of the pin settings. In the arduino IDE, install incbin library for json file to compile with sketch.

The clock code now has 16 pins, which are port C and L. The pin number vs wave number correspondance is:
| Wave number | Digital Pin | Port Number |
| --- | --- | --- |
| 1 | 37 | PC0 |
| 2 | 36 | PC1 |
| 3 | 35 | PC2 |
| 4 | 34 | PC3 |
| 5 | 33 | PC4 |
| 6 | 32 | PC5 |
| 7 | 31 | PC6 |
| 8 | 30 | PC7 |
| 9 | 49 | PL0 |
| 10 | 48 | PL1 |
| 11 | 47 | PL2 |
| 12 | 46 | PL3 |
| 13 | 33 | PL4 |
| 14 | 32 | PL5 |
| 15 | 31 | PL6 |
| 16 | 30 | PL7 |
| ON TIME | 40 | PG1 |

Both the clock part and the trigger FIFO part use port manipulation in Arduino instead of digitalWrite(), since it is much faster and more reliable. I found this youtube video that explains how this works to be a pulse generator: https://www.youtube.com/watch?v=y11JhCXaxZg. See this link for the pin mapping for Arduino Mega 2560: https://docs.arduino.cc/hacking/hardware/PinMapping2560. In the chart, PH0 means port H pin 0, which is the digital pin 17. Pins in the same port are supposed to have better timing consistencies compared to pins in different ports, but that is also acceptable for our intended use.

PROBLEM: It can only be in time (100us) if handling 10 waves or fewer. At 16 waves simultaneously, the duration is ~200us.
