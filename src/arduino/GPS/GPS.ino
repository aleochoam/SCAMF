#include <NMEAGPS.h>
#include <GPSport.h>
#include <Streamers.h>

static NMEAGPS  gps;
static gps_fix  fix;


void setup() {
  Serial.begin(9600);
  gpsPort.begin( 9600 );
}

void loop() {
  
  if(Serial.available()){
    
    
      gps.available( gpsPort );
      fix = gps.read();
      //trace_all( Serial, gps, fix );
      Serial.print(fix);
      Serial.flush();
      
    
  }
}
