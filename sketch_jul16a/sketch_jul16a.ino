#include <Servo.h>

Servo myServo;

int angles[] = {0, 90, 180};  // Allowed angles
int currentAngle = -1;

void setup() {
  myServo.attach(9);           // Connect servo to pin 9
  Serial.begin(9600);
  randomSeed(analogRead(A0));  // Seed random number generator
}

void loop() {
  int newIndex;
  
  // Ensure a new angle different from currentAngle
  do {
    newIndex = random(0, 3);
  } while (angles[newIndex] == currentAngle);
  
  currentAngle = angles[newIndex];
  myServo.write(currentAngle);
  Serial.println(currentAngle);  // Print angle only as number

  delay(2000);  // Wait 2 seconds
}
