#include <Servo.h>

Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(9); // Подключен к пину 9
  myServo.write(0);  // Начальная позиция
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    if (command == '1') {
      myServo.write(180); // Лицо известно
    } else if (command == '0') {
      myServo.write(0); // Лицо неизвестно
    }
  }
}