
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>
#include "Adafruit_VL53L0X.h"
#include <Wire.h>
#include <BH1750.h>
#include <SPI.h>
#include <NMEAGPS.h>
#include <TimerOne.h>


// Sensor de distancia
Adafruit_VL53L0X lox = Adafruit_VL53L0X();

// Sensor de luz
BH1750 lightMeter;

// Sensor de aceleración
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(1010);

// GPS
NMEAGPS  gps;
#define gps_port Serial1
static gps_fix  fix;

// Luces
const int led = 53;
const int pwm = 13;

// Control Luz
double Kp=100, Ki=1, Kd=1;
double error;
double sample;
double lastSample;
double P, I, D;
double Output;

double setPoint;
long lastProcess;


void setup() {
  Serial.begin(9600);
  Serial.flush();
  gps_port.begin( 9600 );

  pinMode(led, OUTPUT);


  lox.begin();
  lightMeter.begin(BH1750::ONE_TIME_HIGH_RES_MODE);
  accel.setRange(ADXL345_RANGE_16_G);
  accel.begin();
  
  setPoint = 3000;

}

void loop() {

  Serial.print("distancia:");
  for(int i = 0; i<5; i++){
    Serial.print(leerDistancia());
    Serial.print(",");
    delay(10);
  }
  Serial.println();
  

  Serial.print("aceleracion:");
  for(int i = 0; i<5; i++){
    Serial.print(leerAceleracion('z'));
    Serial.print(",");
    delay(10);
  }
  Serial.println();

  uint16_t luz = lightMeter.readLightLevel();
  //Serial.print("Luz: ");
  //Serial.println(luz);

  Output = controlLuz();
  analogWrite(pwm, Output);

  if (gps.available( gps_port )) {
    //Serial.read();
    fix = gps.read();
    if (fix.valid.location){
        Serial.print("GPS: ");
        Serial.print( fix.latitude(),5);
        Serial.print(",");
        Serial.print( fix.longitude(),5);
      }else {
        Serial.print( "Posicion invalida" );
      }
      Serial.println();     
   }
  

  if(Serial.available()){
    //Serial.parseInt();
    Timer1.attachInterrupt(apagarLed);
    encenderLed();
    Timer1.initialize(2000000);
    Serial.read();
    /*if (gps.available( gps_port )){
      
      fix = gps.read();
      if (fix.valid.location){
        Serial.print(fix.latitude(),5);
        Serial.print(",");
        Serial.print(fix.longitude(),5);
      }else {
        Serial.print( "Posicion invalida" );
      }
      Serial.println();
    }else{
      Serial.println("No se pudo leer el GPS");
    }*/
  }
  delay(333);
  
}

int leerDistancia(){
  VL53L0X_RangingMeasurementData_t measure;
  lox.rangingTest(&measure, false);
  while(measure.RangeMilliMeter > 5000){
    lox.rangingTest(&measure, false);
  }
  return measure.RangeMilliMeter;
}


double leerAceleracion(char eje){
  double x, y, z;
  sensors_event_t event;
  accel.getEvent(&event);

  if(eje == 'x')
    return event.acceleration.x;
  else if(eje == 'y')
    return event.acceleration.y;
  else
    return event.acceleration.z;
} 


void encenderLed(){
    digitalWrite(led, HIGH);
}

void apagarLed(){
    digitalWrite(led, LOW);
}

double controlLuz(){
  error = setPoint - sample;
  float deltaTime = (millis() - lastProcess) / 1000.0;
  lastProcess = millis();
  
  //P
  P = error * Kp;
  
  //I
  I = I + (error * Ki) * deltaTime;
  
  //D
  D = (lastSample - sample) * Kd / deltaTime;
  lastSample = sample;

  Output = P + I + D;
  Output = Output/100;
  
  if (Output > 255){
    Output = 255;
  }
  else if (Output < 76 && Output > 50){
    Output = 76;
  }
  else {
    Output = 0;
  }
  
  return Output;
}

