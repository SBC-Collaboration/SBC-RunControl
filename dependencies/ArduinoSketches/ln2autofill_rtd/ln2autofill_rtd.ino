// Author: Pedro Rodriguez, Shane Williams
// Last updated: 2025-01-30

const int analogPin_0 = A0; // Analog input pin connected to the scale
const int analogPin_1 = A1; // Analog input pin connected to the scale
const int solenoidPin = 8; // Digital pin connected to the relay/MOSFET controlling the solenoid
const float ThresholdVoltage = 1.3; // Threshold voltage in Volts to open/close solenoid
const unsigned long timeoutDuration = 300000; // 5 minutes in milliseconds

float voltage_0 = 0.0;
float voltage_1 = 0.0;
bool solenoidOpen = false; // State variable to track solenoid status
unsigned long solenoidOpenTime = 0; // Timestamp for when the solenoid was opened

void setup() {
  Serial.begin(9600); // Start serial communication
  pinMode(solenoidPin, OUTPUT); // Set solenoid pin as an output
  digitalWrite(solenoidPin, LOW); // Initialize solenoid to be off (closed)
}

void loop() {
  // Read the analog input (voltage across the resistor)
  int sensorValue_0 = analogRead(analogPin_0);
  int sensorValue_1 = analogRead(analogPin_1);
  
  // Convert the analog reading (0-1023) to a voltage (0-5V)
  voltage_0 = sensorValue_0 * (5.0 / 1024.0);
  voltage_1 = sensorValue_1 * (5.0 / 1024.0);
  
  // Output the voltage to the serial monitor with 2 decimal places
  Serial.print("Voltage: ");
  Serial.print(voltage_0, 2);
  Serial.print("V  ");
  Serial.print(voltage_1, 2);
  Serial.println("V");

  // Control the solenoid based on thresholds and timeout
  unsigned long currentTime = millis();

  if (!solenoidOpen && (voltage_0 > ThresholdVoltage) && (voltage_1 > ThresholdVoltage)) {
    digitalWrite(solenoidPin, HIGH); // Open the solenoid
    solenoidOpen = true;
    solenoidOpenTime = currentTime; // Record the time when opened
    Serial.println("Solenoid OPEN");
  } 
  
  // Close solenoid if input voltage is too low OR timeout occurs
  if (solenoidOpen && ((voltage_0 < ThresholdVoltage && voltage_1 < ThresholdVoltage) || 
      (currentTime - solenoidOpenTime >= timeoutDuration))) {
    digitalWrite(solenoidPin, LOW); // Close the solenoid
    solenoidOpen = false;
    Serial.println("Solenoid CLOSED (Threshold or Timeout)");
  }

  delay(1000); // Delay for readability
}
