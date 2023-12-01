//Created By Ali Adnan
//CMP521A
//November 29th 2023
//This runs a probe temperature

//Libarires
#include <OneWire.h>
#include <DallasTemperature.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2); //Sets up the LCD

#define ONE_WIRE_BUS 8 //Probe PIN

OneWire oneWire(ONE_WIRE_BUS);

DallasTemperature sensors(&oneWire);

float Celsius = 0; //Sets both numbers as decimals
float Fahrenheit = 0;

void setup() {
  sensors.begin();
  lcd.begin(16, 2);
}

void loop() {
  sensors.requestTemperatures(); //Requests Temperatures

  Celsius = sensors.getTempCByIndex(0);
  Fahrenheit = sensors.toFahrenheit(Celsius);

  lcd.setCursor(0, 0);
  lcd.print(Celsius);
  lcd.print(" Celsius  ");
  lcd.setCursor(0, 1);
  lcd.print(Fahrenheit);
  lcd.println(" Fahrenheit ");

  delay(100);

}
