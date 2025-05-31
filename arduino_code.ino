const int lm35Pin = A0; // LM35 analog pin
const int ldrPin = A1;  // LDR analog pin

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Read LM35 and convert to Celsius
  int lm35Value = analogRead(lm35Pin);
  float voltage = lm35Value * (5.0 / 1023.0);
  float temperatureC = voltage * 100.0;

  // Read LDR value (0 - 1023)
  int lightLevel = analogRead(ldrPin);

  // Send over Serial in key:value format
  Serial.print("TEMP:");
  Serial.print(temperatureC);
  Serial.print(";LIGHT:");
  Serial.println(lightLevel);

  delay(2000);
}
