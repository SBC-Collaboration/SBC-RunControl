// Author: Pedro Rodriguez

const int analogPin = A0; // Analog input pin connected to the scale
const int solenoidPin = 8; // Digital pin connected to the relay/MOSFET controlling the solenoid
const float lowerThresholdWeight = 108.0; // Lower threshold weight in units to open the solenoid
const float upperThresholdWeight = 126.0; // Upper threshold weight in units to close the solenoid

float weight = 0.0;
float current_mA = 0.0;
float voltage = 0.0;
bool solenoidOpen = false; // State variable to track solenoid status

void setup() {
  Serial.begin(9600); // Start serial communication
  pinMode(solenoidPin, OUTPUT); // Set solenoid pin as an output
  digitalWrite(solenoidPin, LOW); // Initialize solenoid to be off (closed)
}

void loop() {
  // Read the analog input (voltage across the resistor)
  int sensorValue = analogRead(analogPin);
  
  // Convert the analog reading (0-1023) to a voltage (0-5V)
  voltage = sensorValue * (5.0 / 1023.0);
  
  // Convert the voltage to current in mA 
  current_mA = voltage / 250.0 * 1000.0; // Convert to milliamps
  
  // Ensure current is within expected 4-20 mA range
  if (current_mA < 4.0) current_mA = 4.0;
  if (current_mA > 20.0) current_mA = 20.0;

  // Custom mapping of current (4-20 mA) to weight (0-300 units)
  weight = mapFloat(current_mA, 4.0, 20.0, 0.0, 300.0);
  
  // Output the weight to the serial monitor with 2 decimal places
  Serial.print("Weight: ");
  Serial.print(weight, 2); // Print weight with 2 decimal places
  Serial.println(" units");

  // Control the solenoid based on lower and upper thresholds
  if (!solenoidOpen && weight < lowerThresholdWeight) {
    digitalWrite(solenoidPin, HIGH); // Open the solenoid
    solenoidOpen = true;
    Serial.println("Solenoid OPEN");
  } else if (solenoidOpen && weight > upperThresholdWeight) {
    digitalWrite(solenoidPin, LOW); // Close the solenoid
    solenoidOpen = false;
    Serial.println("Solenoid CLOSED");
  }
  
  delay(1000); // Delay for readability
}

// Custom map function for floating-point values
float mapFloat(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
