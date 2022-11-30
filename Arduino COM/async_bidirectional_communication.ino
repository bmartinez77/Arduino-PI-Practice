// initialize variables
int count = 0;
unsigned long lastTimeActionDone = millis();
unsigned long actionDelay = 500;

void setup() {
 // initialize serial with the port
  Serial.begin(115200);
  while (!Serial) {}
}

void loop() {
unsigned long timeNow = millis();
  if (timeNow - lastTimeActionDone >= actionDelay) {
    lastTimeActionDone = timeNow;
    Serial.println(count);
      count++;
  }

  // read serial 
  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');

    if (cmd == "reset") {
      count = 0;
    } 
    else {
      
    }
  }
}
