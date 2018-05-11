#include "Adafruit_VL53L0X.h"

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void setup() {
  Serial.begin(9600);

  // wait until serial port opens for native USB devices
  while (!Serial) {
    delay(1);
  }
  if (!lox.begin()) {
    while(1);
  }
}


void loop() {
  VL53L0X_RangingMeasurementData_t measure;

  for(int i = 0; i<5; i++){
    lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
  
    if (measure.RangeStatus != 4) {  // phase failures have incorrect data
      Serial.print(measure.RangeMilliMeter); Serial.print(",");
    }
    delay(100);
  }
  
  Serial.println();  
  delay(100);
}
