#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

/* Assign a unique ID to this sensor at the same time */
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(1010);


void setup(void) 
{
  Serial.begin(9600);
  //Serial.println("Aceleration in Z-Axis"); Serial.println("");
  
  /* Initialise the sensor */
  if(!accel.begin())
  {
    // There was a problem detecting the ADXL345 ... check your connections
    Serial.println("Ooops, no ADXL345 detected ... Check your wiring!");
    while(1);
  }

  /* Set the range to whatever is appropriate for your project */
  accel.setRange(ADXL345_RANGE_16_G);
  // displaySetRange(ADXL345_RANGE_8_G);
  // displaySetRange(ADXL345_RANGE_4_G);
  // displaySetRange(ADXL345_RANGE_2_G);
  
  /* Display some basic information on this sensor */
  //displaySensorDetails();
  
  /* Display additional settings (outside the scope of sensor_t) */
  // displayDataRate();
  // displayRange();
  // Serial.println("");
}

void loop(void) 
{
  /* Get a new sensor event */ 
  sensors_event_t event;
  if(Serial.available()){
    Serial.parseInt();
    delay(100);
    for(int i = 0; i< 5; i++){
      accel.getEvent(&event);
      Serial.print(event.acceleration.z);
      Serial.print(",");
      delay(100);
    }
    Serial.println();  
    
  }
  
}
