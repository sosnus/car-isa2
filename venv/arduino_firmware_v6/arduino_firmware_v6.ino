#include <Servo.h>

Servo camera_H;
Servo camera_V;
Servo motor_L;
Servo motor_R;

uint8_t servo205 = 90;
uint8_t servo206 = 90;
uint8_t servo209 = 89;
uint8_t servo210 = 89;

#define cmdCH 205
#define cmdCV 206
#define cmdML 209
#define cmdMR 210

int receiv = 90;

uint8_t receiv2 = 90;

void setup() {
  camera_H.attach(5);
  camera_V.attach(6);
  motor_L.attach(9);
  motor_R.attach(10);
  camera_H.write(servo205);
  camera_V.write(servo206);
  motor_L.write(servo209);
  motor_R.write(servo210);
  Serial.begin(19200);
  Serial.print("\n\rTEST, SETUP() ");
}

void loop() {
//  delay(1000);

//  Serial.print("new: ");
//  Serial.println(Serial.available());

  if ( Serial.available())
  {
    receiv = Serial.read();
    if (receiv >= cmdCH && receiv <= cmdMR)
    {
      // NEW COMMAND

      delay(25); //wait for new char - value of command
      receiv2 = Serial.read();
      if(receiv2 > 120 || receiv2 < 70) receiv2 = 89;
   //   receiv2 = (receiv2 - 64) * 5;
         if(true)
      {
      Serial.print("  R: ");
      Serial.print(receiv);
      Serial.print("=" );
      Serial.print(receiv2);
  }
  
      if (receiv == cmdCH) // camera Horyzont
      {
        servo205 = receiv2;
        camera_H.write(servo205);
        Serial.println("edit CamH");
      }    
      else if (receiv == cmdCH) // servoParachute
      {
        servo206 = receiv2;
     //   if(servo206<75) servo206 = 75;
     //   if(servo206>135) servo206 = 135;
        camera_V.write(servo206);
        Serial.println("edit CamV");
      }
      else if (receiv == cmdML) // servoParachute
      {
        servo209 = receiv2;
        motor_L.write(servo209);
  ///      Serial.println("edit MotorL");
      }
      else if (receiv == cmdMR) // servoParachute
      {
        servo210 = receiv2;
        motor_R.write(servo210);
  ///      Serial.println("edit MotorR");
      }
      else
      {
        Serial.println("ERR, bad command");
      }
    }
  }
}
