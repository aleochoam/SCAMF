#define puertoLed 13
#define puertoFotoR 0

void setup() {
  pinMode(puertoFotoR, INPUT);
  pinMode(puertoLed, OUTPUT);

}

void loop() {
  int intensidad = 255;
  analogWrite(puertoLed, intensidad);

}
