
#include "DHT.h"

#define DHTPIN 2 // what pin we're connected to

//Define the DHT module type
#define DHTTYPE DHT11 //DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
Serial.begin(9600);
Serial.println("DHT11 test!");

dht.begin();
}

void loop() {
float h = dht.readHumidity();
float c = dht.readTemperature();
// if the sensor is not working, this will halt the Arduino
if (isnan(h) || isnan(c)) {
Serial.println("DHT sensor read failure.");
return;
}
Serial.println("Humidity: " + String(h) + "%");
Serial.println("Temperature: " + String(c) + "C");
delay(1000); // wait 3 seconds
}