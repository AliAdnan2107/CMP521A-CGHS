//Created By Ali Adnan
//CMP521A
//November 3rd 2023
//This program will get a button to turn on a light and spin the servo 40 degrees and back.


//Variables
const int buttonPin = 4;  // the number of the pushbutton pin
const int ledPin = 6;    // the number of the LED pin
int buttonState = 0;  // variable for reading the pushbutton status
int pos = 0; // variable to store servo's position
#include <Servo.h>
Servo myservo;

//Code
void setup() {
  // initialize the LED pin and Servo pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  // attach servo to pin
  myservo.attach(8);
}

void loop() {
  buttonState = digitalRead(buttonPin); //If button is pressed
  if (buttonState == LOW) {
    digitalWrite(ledPin, HIGH); // turn LED on
    for (pos = 0; pos <= 40; pos += 1) { // turn servo 40 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
  for (pos = 40; pos >= 0; pos -= 1) { // turn servo back to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
  }
  else {
    digitalWrite(ledPin, LOW); // turn LED off
  }
}
