//Created By Ali Adnan
//CMP521A
//October 31st 2023
//This program will get a button to turn on a light.


//Variables
const int buttonPin = 2;  // the number of the pushbutton pin
const int ledPin = 13;    // the number of the LED pin
int buttonState = 0;  // variable for reading the pushbutton status

//Code
void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {  //If Button pressed
    // turn LED on:
    digitalWrite(ledPin, HIGH);
  } else { //If Not
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
}