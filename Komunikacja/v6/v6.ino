#include <Servo.h>

Servo camera_H;
Servo camera_V;
Servo motor_L;
Servo motor_R;

uint8_t servo205 = 90;
uint8_t servo206 = 90;
uint8_t servo209 = 89;
uint8_t servo210 = 89;

#define cmdCV 209
#define cmdCH 210
#define cmdML 211
#define cmdMR 212

int receiv = 89;

uint8_t receiv2 = 89;

void setup() {
  camera_H.attach(5);
  camera_V.attach(6);
  motor_L.attach(9);
  motor_R.attach(10);

  camera_H.write(servo205);
  camera_V.write(servo206);
  motor_L.write(servo209);  
  motor_R.write(servo210);
  Serial.begin(9600);
  Serial.print("\n\rTEST, SETUP() ");
}

void loop() {
//  delay(1000);

//  Serial.print("new: ");
//  Serial.println(Serial.available());

  if ( Serial.available())
  {
    receiv = Serial.read();
    if (receiv >= cmdCV && receiv <= cmdMR)
    {
      // NEW COMMAND
      Serial.print("\n\rReveive: ");
      Serial.print(receiv);
      Serial.print("=" );
      delay(50); //wait for new char - value of command
      receiv2 = Serial.read();
   //   receiv2 = (receiv2 - 64) * 5;
      Serial.println(receiv2);

      if (receiv == cmdCV) // servoDrop
      {
        servo205 = receiv2;
        camera_H.write(servo205);
        Serial.println("edit CamV");
      }    
      else if (receiv == cmdCH) // servoParachute
      {
        servo206 = receiv2;
        camera_V.write(servo206);
        Serial.println("edit CamH");
      }
      else if (receiv == cmdML) // servoParachute
      {
        servo209 = receiv2;
        motor_L.write(servo209);
        Serial.println("edit MotorL");
      }
      else if (receiv == cmdMR) // servoParachute
      {
        servo210 = receiv2;
        motor_R.write(servo210);
        Serial.println("edit MotorR");
      }
      else
      {
        Serial.println("ERR, bad command");
      }
    }
  }
}
