// create variables 
unsigned long lastTimeActionDone = millis();
unsigned long actionDelay = 1000;


// send temp 
// recieve dat from serial --> power on/off LED

void setup() {
 // initialize serial with the port
  Serial.begin(115200);
  while (!Serial) {}

  // initialize pin
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  unsigned long timeNow = millis();
  if (timeNow - lastTimeActionDone >= actionDelay) {
    lastTimeActionDone = timeNow;
    // do action
    
    int randomNumber = random(5, 25);

    Serial.println(randomNumber);
  }

  // read serial 
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');

    // if message is on
    if (message == "on") {
      digitalWrite(13, HIGH);
    }
    
    // if message is off
    else if (message == "off") {
      digitalWrite(13, LOW);

    }

    else {
      
    }
  }
}
