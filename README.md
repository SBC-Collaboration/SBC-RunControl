# Arduino-GateGenerator
Generates the gates that control image acquisition and illumination for SBC

Note by Zhiheng:\
Both the clock part and the trigger FIFO part use port manipulation in Arduino instead of digitalWrite(), since it is much faster and more reliable. I found this youtube video that explains how this works to be a pulse generator: https://www.youtube.com/watch?v=y11JhCXaxZg. See this link for the pin mapping for Arduino Mega 2560: https://docs.arduino.cc/hacking/hardware/PinMapping2560. In the chart, PH0 means port H pin 0, which is the digital pin 17. Pins in the same port are supposed to have better timing consistencies compared to pins in different ports, but that is also acceptable for our intended use.
