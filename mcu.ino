void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {

    String command = Serial.readStringUntil('\n');

    if (command == "DISPENSE 2 30") {
      Serial.println("ACK");

      delay(1000);

      Serial.println("WEIGHT 30.2");
    }
  }
}
