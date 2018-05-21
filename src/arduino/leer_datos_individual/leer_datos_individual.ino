#include <SparkFun_ADXL345.h> 

ADXL345 adxl = ADXL345();

void setup() {
  Serial.begin(9600);  
  adxl.powerOn();            
  adxl.setRangeSetting(16); 

}

void loop() {
  if(Seria.available()){
    Serial.read();
    for(int i = 0; i<5; i++){
      Serial.print(leerAceleracion('z'));
      Serial.print(",");
    }
  }

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
