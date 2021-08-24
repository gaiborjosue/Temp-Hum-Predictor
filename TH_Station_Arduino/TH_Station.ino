#include <U8glib.h>
#include <SoftwareSerial.h>
#include <RTClib.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SimpleDHT.h>


#include "DHT.h"
#define DHTPIN 8
#define DHTTYPE DHT22 

LiquidCrystal_I2C lcd(0x27,16,2);

// for DHT11,
//      VCC: 5V or 3V
//      GND: GND
//      DATA: 2
//int pinDHT22 = 8;
//int pushButton = 2;

DHT dht(DHTPIN, DHTTYPE);
RTC_DS3231 rtc;      // crea objeto del tipo RTC_DS3231

//int sensor_arroz_pin = ;

#define SSID2 "CNT_FLIAGAIBOR" // "WiFiname" Bioinv_IOT
#define PASS "orion1974" // "Password" biosfera2josue
#define AUTH "sanaIi1SHwpWbWnVj8U6_aNrDJycYY_I"
#define IP "184.106.153.149" // thingspeak.com ip (do not change)
String msg = "GET /update?api_key=ORUGFBB8N8QG704Q"; //change it with your channel Write key
const int Time_S = 120; //Change this to your prefered sampling interval in seconds, exampe 2 min is 120 seconds
float Temp_C;
float Temp_F;
float Humidity;


////////////////////////////////////////////////////////////////////////////////////////////////
void dh_setup() {
  Serial.println("Sample DHT22...");
  Serial.println("Temperature and Humidity Data");
  dht.begin();
}

////////////////////////////////////////////////////////////////////////////////////////////////
void lc_setup() {
  lcd.init();
  lcd.backlight();
  lcd.clear();
}
/////////////////////////////////////////////////////////////////////////////////////////////////
void setup() {
  Serial.begin(115200);
  // start working...
  Serial.println("AT");
  delay(5000);
  if (Serial.find("OK")) {
    connectWiFi();
  }
  dh_setup();
  // make the pushbutton's pin an input:
  //pinMode(pushButton, INPUT_PULLUP);

  if (! rtc.begin()) {        // si falla la inicializacion del modulo
    Serial.println("Modulo RTC no encontrado !");  // muestra mensaje de error
    while (1);         // bucle infinito que detiene ejecucion del programa
  }
  //rtc.adjust(DateTime(__DATE__,__TIME__));
  
  lc_setup();
  //pinMode(sensor_arroz_pin, INPUT);
  lcd.backlight();
}
///////////////////////////////////////////////////////////////////////////////////////////////
void loop() {
  DateTime fecha = rtc.now();
  
  // read the input pin:
  //int buttonState = digitalRead(pushButton);
  // delay in between reads for stability
  //delay(250);
  // read without samples.
  byte temperature = 0;
  byte humidity = 0;

  int err = SimpleDHTErrSuccess;
  //if ((err = dht22.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
    //Serial.print("Read DHT11 failed, err="); Serial.print(SimpleDHTErrCode(err));
    //Serial.print(","); Serial.println(SimpleDHTErrDuration(err)); delay(1000);
    //return;
  //}

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  
  Serial.print(t); Serial.print(" *C, ");
  Serial.print(h); Serial.println(" H");
  
  Temp_C = t;
  Humidity = h;

  lcd.setCursor(0, 0);
  lcd.print("T: ");
  lcd.print(t);
  lcd.print("C");
  lcd.setCursor(10, 0);
  lcd.print(fecha.hour());
  lcd.print(":");
  lcd.print(fecha.minute());
  lcd.setCursor(0, 1);
  lcd.print("H: ");
  lcd.print(h);
  lcd.print("%");
  
  /////IF STATEMENTS /////////
  if (fecha.minute() == 0 && fecha.seconds() == 15 || fecha.minute() == 15 && fecha.seconds() == 15 || fecha.minute() == 30 && fecha.seconds() == 15 || fecha.minute() == 45 && fecha.seconds() == 15 ) {
    Send();
    delay(1000);
  }
}

void Send() {
  String cmd = "AT+CIPSTART=\"TCP\",\"";
  cmd += IP;
  cmd += "\",80";
  Serial.println(cmd);
  delay(2500);
  cmd = msg ;
  cmd += "&field1="; //field 1 for test value
  cmd += Temp_C; //change to temp_F for Fahrenheit
  cmd += "&field2="; //field
  cmd += Humidity;
  //cmd += "&field3="; //field
  //cmd += sustratoAPercentValue;
  //cmd += "&field4="; //field
  //cmd += sustratoPPercentValue;
  //cmd += "&field5="; //field
  //cmd += 100;
  //cmd += "&field6="; //field
  //cmd += 1000;
  //cmd += "&field7="; //field
  //cmd += 100;
  //cmd += "&field8="; //field
  //cmd += 100;
  cmd += "\r\n";
  cmd += "\r\n";
  Serial.print("AT+CIPSEND=");
  Serial.println(cmd.length());
  if (Serial.find(">")) {
    Serial.print(cmd);
  } else {
    Serial.println("AT+CIPCLOSE");
  }
}

boolean connectWiFi() {
  Serial.println("AT+CWMODE=1");
  delay(2000);
  String cmd = "AT+CWJAP=\"";
  cmd += SSID2;
  cmd += "\",\"";
  cmd += PASS;
  cmd += "\"";
  Serial.println(cmd);
  delay(5000);
  if (Serial.find("OK")) {
    return true;
  } else {
    return false;
  }
}
