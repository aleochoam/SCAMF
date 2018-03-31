#define puertoAcelerometro 22
#define puertoProximidad 23

void setup() {
  Serial.begin(9600);
  pinMode(puertoAcelerometro, INPUT);
  pinMode(puertoProximidad, INPUT);
  

}

void loop() {
  int aceleracion = analogRead(puertoAceleracion);
  Serial.print('a');
  Serial.println(aceleracion);

  
  int proximidad = analogRead(puertoProximidad);
  Serial.print('a');
  Serial.println(aceleracion);

}
