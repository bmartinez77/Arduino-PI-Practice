void setup() {
  // initialize pin
  pinMode(13, OUTPUT);

  // initialize serial
  Serial.begin(115200);
  while (!Serial){}
  
}

void loop() {
// check for messages 
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');

    // if message is on
    if (message == "on") {
      digitalWrite(13, HIGH);
      Serial.println(message);
    }
    
    // if message is off
    else if (message == "off") {
      digitalWrite(13, LOW);
      Serial.println(message);

    }

    else {
      
    }
    
  }

  
  // Test LED
  //  digitalWrite(13, HIGH);
  //  delay(1200);
  //  
  //  digitalWrite(13, LOW);
  //  delay(1200);

}
