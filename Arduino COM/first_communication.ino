int counter = 0;

void setup() {
  // initialize serial with the port
  Serial.begin(115200);
  while (!Serial) {}
  
}

void loop() {
  if (Serial.available() > 0){
    String message = Serial.readStringUntil('\n');
    message = message + " " + String(counter);
    counter++;
    Serial.println(message);
  }

  
  // Send data to pi
  // Serial.println("Hello from Arduino");
  // delay(1000);
}
