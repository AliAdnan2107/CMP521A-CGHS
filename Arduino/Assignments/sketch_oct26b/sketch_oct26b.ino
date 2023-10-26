//Created By Ali Adnan
//CMP521A
//OCT. 26th 2023
//This program will blink through both lights (One on at a time)



void setup() {
  // put your setup code here, to run once:
  pinMode(5, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(5, HIGH); //Turn On (Blue Light)
  delay(2000);                    // Stay On (Red Light)
  digitalWrite(5, LOW);  // Turn Off (Blue Light)
  digitalWrite(10, HIGH); //Turn On (Red Light)
  delay(2000);                    // Stay On (Red Light)
  digitalWrite(10, LOW); // Turn Off (Red Light)

}
