//Created By Ali Adnan
//CMP521A
//This program turns on a red light when photoresistor reads low levels and green when photoresistor is high
//November 8th 2023

//Variables
#define PHOTOCELL 0 // used with analogRead
const int ledPinRed = 8;
const int ledPinGreen = 9;
const int speakerPin = 10;

//Setup And Code
void setup() {
Serial.begin(9600); // allow USB console connection
pinMode(ledPinRed, OUTPUT); // Setup for all lights
pinMode(ledPinGreen, OUTPUT);
pinMode(speakerPin, OUTPUT);
}

void loop() {
int value = analogRead(PHOTOCELL); // uses defined symbol
Serial.println(value); // Print Value into serial monitor
delay(10);
if (value < 30) { //If value is under 30, Turn red light and speaker on
  digitalWrite(ledPinRed, HIGH);
  digitalWrite(speakerPin, HIGH);
  digitalWrite(ledPinGreen, LOW);
} else if (value >= 40) { //If value is above 30, Turn green light
  digitalWrite (ledPinRed, LOW);
  digitalWrite (speakerPin, LOW);
  digitalWrite (ledPinGreen , HIGH);
}
}