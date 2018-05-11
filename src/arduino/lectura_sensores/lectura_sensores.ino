#include "Adafruit_VL53L0X.h"
#include <Wire.h>
#include <BH1750.h>
#include <SPI.h>
#include <SparkFun_ADXL345.h> 

// Sensor de distancia
Adafruit_VL53L0X lox = Adafruit_VL53L0X();

// Sensor de luz
BH1750 lightMeter;

// Sensor de aceleración
ADXL345 adxl = ADXL345();

void setup() {
  Serial.begin(9600);
  Wire.begin();

  lox.begin();
  lightMeter.begin();
  adxl.powerOn();            
  adxl.setRangeSetting(16); 
}

void loop() {
  Serial.print("distancia,");
  for(int i = 0; i<5; i++){
    Serial.print(leerDistancia());
    Serial.print(",");
  }
  Serial.println();

  Serial.print("aceleracion");
  for(int i = 0; i<5; i++){
    Serial.print(leerAceleracion('z'));
    Serial.print(",");
  }
  Serial.println();
}

int leerDistancia(){
  VL53L0X_RangingMeasurementData_t measure;
  do{
    lox.rangingTest(&measure, false);  
  }while(measure.RangeStatus != 4);

  return measure.RangeMilliMeter;
}

uint16_t leerLuz(){
  return lightMeter.readLightLevel();
}

int leerAceleracion(char eje){
  int x, y, z;
  adxl.readAccel(&x, &y, &z);

  if(eje == 'x')
    return x;
  else if(eje == 'y')
    return y;
  else
    return z;
} 

