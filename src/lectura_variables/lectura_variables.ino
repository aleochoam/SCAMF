#define puertoAcelerometro 12
#define puertoProximidad 13

void setup() {
  Serial.begin(9600);
  pinMode(puertoAcelerometro, INPUT);
  pinMode(puertoProximidad, INPUT);


}

void loop() {

  int aceleracion = analogRead(puertoAcelerometro);
  Serial.print('a');
  Serial.println(aceleracion);

  delay(500);
  int proximidad = analogRead(puertoProximidad);
  Serial.print('p');
  Serial.println(proximidad);

  delay(500);

}
