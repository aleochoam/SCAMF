// #include <SparkFun_ADXL345.h>
#include "Adafruit_VL53L0X.h"

// ADXL345 adxl = ADXL345();
Adafruit_VL53L0X lox = Adafruit_VL53L0X();
void setup() {

  Serial.begin(9600);
  // adxl.powerOn();
  // adxl.setRangeSetting(16);
  lox.begin();

}

void loop() {
  if(Serial.available()){
    delay(500);
    Serial.read();
    for(int i = 0; i<5; i++){
      // Serial.print(leerAceleracion('z'));
      Serial.print(leerDistancia());
      Serial.print(",");
      delay(10);
    }
    Serial.println();
  }

}

// int leerAceleracion(char eje){
//   int x, y, z;
//   adxl.readAccel(&x, &y, &z);

//   if(eje == 'x')
//     return x;
//   else if(eje == 'y')
//     return y;
//   else
//     return z;
// }



int leerDistancia(){
  VL53L0X_RangingMeasurementData_t measure;
  lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
  return measure.RangeMilliMeter;
}


