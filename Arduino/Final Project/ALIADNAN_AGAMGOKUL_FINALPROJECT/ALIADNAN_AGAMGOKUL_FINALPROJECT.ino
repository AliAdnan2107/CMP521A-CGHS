/*
Created By Ali Adnan & Agam Gokul
CMP521A
Arduino Final Project
This Project will open a door using a lock connected to a RFID/NFC Lock System
November 28th 2023
*/
 
// Libraries And Variables
#include <LiquidCrystal_I2C.h> // Liquid crystal library
#include <Servo.h> // Servo Library
#include <SPI.h> // SPI.H library
#include <MFRC522.h> // MRFC522 library
Servo myservo1; // Servo 1
Servo myservo2;  // Servo 2                                                                                           
#define SS_PIN 10 // RFID Data Pin
#define RST_PIN 9 // RFID Reader Pin
#define ServoPin1 A1 // Servo Pin 1
#define ServoPin2 A2 // Servo Pin 2

String UID = "4C DC 24 D9"; //Unique code to RFID
byte lock = 0; //Lock Variable

LiquidCrystal_I2C lcd(0x27, 16, 2); // Initialize LCD
MFRC522 rfid(SS_PIN, RST_PIN); // Initialize RFID Reader

const int greenledPin1 =  7; // Green LED 1
const int greenledPin2 =  6; // Green LED 2
const int blueledPin1 =  5; // Blue LED 1
const int blueledPin2 =  4; // Blue LED 2
const int speakerPin =  2; // Speaker Pin 1
const int redledPin1 =  3; // Red LED Pin 1
const int redledPin2 =  8;  // Red LED Pin 2
int lockState = 0; // Lock State

// Setup Code
void setup() {
  Serial.begin(9600); // Begin Serial
  lcd.init(); //Initialize LCD
  lcd.backlight();
  
  SPI.begin(); // Start RFID Reader.

  rfid.PCD_Init(); // Initialize All Pins
  pinMode(greenledPin1, OUTPUT);
  pinMode(greenledPin2, OUTPUT);
  pinMode(blueledPin1, OUTPUT);
  pinMode(blueledPin2, OUTPUT);
  pinMode(redledPin1, OUTPUT);
  pinMode(redledPin2, OUTPUT);
  pinMode(speakerPin, OUTPUT);
  myservo1.attach(ServoPin1); // Attach Servo's
  myservo2.attach(ServoPin2);
  myservo1.write(180); // Set Servo's to Lock Position
  myservo2.write(0);
}

// Loop Code
void loop() {
  //Set LCD
  lcd.setCursor(2, 0);
  lcd.print("Enter/Exit");
  lcd.setCursor(1, 1);
  lcd.print("Place your ID");
 
  // If RFID Chip Is Detected, Read it.
  if ( ! rfid.PICC_IsNewCardPresent())
    return; //Return Result
  if ( ! rfid.PICC_ReadCardSerial())
    return;

  // Clear LCD and Scan
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Scanning");

  Serial.print("NUID tag is :"); // Checks if Tag ID Matches Unique ID
  String ID = "";
  // Scanning Light Pins and process
  for (byte i = 0; i < rfid.uid.size; i++) {
    lcd.print(".");
    ID.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
    ID.concat(String(rfid.uid.uidByte[i], HEX));
    digitalWrite(blueledPin1, HIGH);
    digitalWrite(blueledPin2, HIGH);
    delay(500);
    digitalWrite(blueledPin1, LOW);
    digitalWrite(blueledPin2, LOW);
  }
  ID.toUpperCase();

  // If ID Matches, Unlock Door.
  if (ID.substring(1) == UID && lock == 0 ) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Welcome");
    myservo1.write(0);
    myservo2.write(180);
    digitalWrite(greenledPin1, HIGH);
    digitalWrite(greenledPin2, HIGH);
    delay(1500);
    digitalWrite(greenledPin1, LOW);
    digitalWrite(greenledPin2, LOW);
    lcd.clear();
    lock = 1;

    // If ID Matches, Lock Door
  } else if (ID.substring(1) == UID && lock == 1 ) {

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Goodbye");
    myservo1.write(180);
    myservo2.write(0);
    digitalWrite(greenledPin1, HIGH);
    digitalWrite(greenledPin2, HIGH);
    delay(1500);
    digitalWrite(greenledPin1, LOW);
    digitalWrite(greenledPin2, LOW);
    lcd.clear();
    lock = 0;
    //If ID Doesn't Match, Yell At Them.
  } else {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Wrong card!");
    digitalWrite(redledPin1, HIGH);
    digitalWrite(redledPin2, HIGH);
    digitalWrite(speakerPin, HIGH);
    delay(1500);
    digitalWrite(redledPin1, LOW);
    digitalWrite(redledPin2, LOW);
    digitalWrite(speakerPin, LOW);
    lcd.clear();
  }
}
