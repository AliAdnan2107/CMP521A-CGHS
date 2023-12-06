/*Door lock system code
 * https://srituhobby.com
 */

#include <Servo.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>
#include <IRremote.h>

#define SS_PIN 10
#define RST_PIN 9
String UID = "20 9B 25 D9";
byte lock = 0;
int IRPIN = 8;          //  The digital pin that the signal pin of the sensor is connected to
IRrecv irrecv(IRPIN);
decode_results results;     //  A varuable that would be used by receiver to put the key code into
Servo servo;
LiquidCrystal_I2C lcd(0x27, 16, 2);
MFRC522 rfid(SS_PIN, RST_PIN);


void setup() {
  Serial.begin(9600);
  servo.write(70);
  lcd.init();
  lcd.backlight();
  servo.attach(A3);
  SPI.begin();
  rfid.PCD_Init();
  IrReceiver.begin(IRPIN, ENABLE_LED_FEEDBACK);
}

void loop() {
  lcd.setCursor(4, 0);
  lcd.print("Welcome!");
  lcd.setCursor(1, 1);
  lcd.print("Tap your card");
  delay(1000);
  lcd.clear();
  lcd.setCursor(4, 0);
  lcd.print("Welcome!");
  lcd.setCursor(1, 1);
  lcd.print("Or Use Keypad");
  delay(1000);


  if (!rfid.PICC_IsNewCardPresent())
    return;
  if (!rfid.PICC_ReadCardSerial())
    return;

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Scanning");
  Serial.print("NUID tag is :");
  String ID = "";
  for (byte i = 0; i < rfid.uid.size; i++) {
    lcd.print(".");
    ID.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
    ID.concat(String(rfid.uid.uidByte[i], HEX));
    delay(300);
  }
  ID.toUpperCase();

  if (ID.substring(1) == UID && lock == 0) {
    servo.write(70);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Door is locked");
    delay(1500);
    lcd.clear();
    lock = 1;
  } else if (ID.substring(1) == UID && lock == 1) {
    servo.write(160);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Door is open");
    delay(1500);
    lcd.clear();
    lock = 0;
  } else {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Wrong card!");
    delay(1500);
    lcd.clear();
  }
  if (IrReceiver.decode()) {
    Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);
    if (IrReceiver.decodedIRData.decodedRawData == 0xE31CFF00) {
      lcd.setCursor(0,0);
      lcd.print("Remote Control Detected");
      lcd.setCursor(0,1);
      lcd.print("Please Wait.");
      servo.write(160);
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Door is Unlocked");
      delay(1500);
      lcd.clear();
      lock = 1;
    }
  IrReceiver.resume();
  }
}