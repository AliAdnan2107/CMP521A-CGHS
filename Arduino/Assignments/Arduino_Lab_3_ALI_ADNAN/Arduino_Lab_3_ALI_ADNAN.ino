//Created By Ali Adnan
//CMP521A
//October 31st 2023
//This program will get a button to turn on a light.


//Variables
const int buttonPin = 4;    // the number of the pushbutton pin
const int ledPin = 7;       // the number of the LED pin
const int SpeakerPin = 10;  // the number of the Speaker pin
int buttonState = 0;        // variable for reading the pushbutton status

//Code
void setup() {
  // initializing the LED Pin And Speaker PIN To get an output from button
  pinMode(ledPin, OUTPUT);
  pinMode(SpeakerPin, OUTPUT);
  // initialize the button to Activate the speaker and LED:
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {  //If Button pressed
    // turn LED on, and Speaker:
    digitalWrite(ledPin, HIGH);
    digitalWrite(SpeakerPin, HIGH);
  } else {  //If Not
    // turn LED off, And Speaker:
    digitalWrite(ledPin, LOW);
    digitalWrite(SpeakerPin, LOW);
  }
}