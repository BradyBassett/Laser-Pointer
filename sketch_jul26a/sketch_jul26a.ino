#include <Servo.h>

Servo servoX, servoY;

String serialData;

void setup() { 
  servoY.attach(10);
  servoX.attach(9);
  Serial.begin(9600);
  Serial.setTimeout(10);

} 

void loop() {
  
}

void serialEvent(){
  serialData = Serial.readString();

  servoX.write(parseDataX(serialData));
  servoY.write(parseDataY(serialData));
}

int parseDataX(String data){
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);
  return data.toInt();
}

int parseDataY(String data){
  data.remove(0, data.indexOf("Y") + 1);

  return data.toInt();
}
