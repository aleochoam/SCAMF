// #include <SparkFun_ADXL345.h>
#include "Adafruit_VL53L0X.h"

#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

Adafruit_VL53L0X lox = Adafruit_VL53L0X();
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(1010);

void setup() {

  Serial.begin(9600);
  lox.begin();
  accel.setRange(ADXL345_RANGE_16_G);

}

void loop() {
  if(Serial.available()){
    Serial.read();
    for(int i = 0; i<5; i++){
      Serial.print(leerAceleracion('z'));
      //Serial.print(leerDistancia());
      Serial.print(",");
      delay(10);
    }
    Serial.println();
  }

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


int leerDistancia(){
  VL53L0X_RangingMeasurementData_t measure;
  lox.rangingTest(&measure, false);
  while(measure.RangeMilliMeter > 5000){
    lox.rangingTest(&measure, false);
  }
  return measure.RangeMilliMeter;
}


