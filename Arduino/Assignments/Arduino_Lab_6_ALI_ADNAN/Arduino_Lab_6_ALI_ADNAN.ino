#include <FastIO.h>
#include <I2CIO.h>
#include <LCD.h>
#include <LiquidCrystal.h>
#include <LiquidCrystal_I2C.h>
#include <LiquidCrystal_I2C_ByVac.h>
#include <LiquidCrystal_SI2C.h>
#include <LiquidCrystal_SR.h>
#include <LiquidCrystal_SR1W.h>
#include <LiquidCrystal_SR2W.h>
#include <LiquidCrystal_SR3W.h>
#include <SI2CIO.h>
#include <SoftI2CMaster.h>

//Created by Ali Adnan
//CMP521A
//This is a water level sensor that will display the water level on a LCD display
//November 21st 2023

#include <LiquidCrystal.h>
LiquidCrystal lcd(2,3,8,9,10,11);

int resval = 0;
int respin = A4;

void setup(){

  lcd.begin(16,2);
  lcd.print (" WATER LEVEL: ");
  Serial.begin(9600);
}

void loop(){
  lcd.setCursor(0,1);
  resval = analogRead(respin);
    Serial.println(resval);
    delay(10);
  if (resval<=210){
    lcd.println("Empty");
  }
  else if (resval>210 && resval<=300){
    lcd.println("Low");
  }
  else if (resval>300 && resval<=330) {
    lcd.println("Medium");
  }
  else if (resval>330){
    lcd.println("High");
  }
  delay(1000);
}