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
 // Serial.print("\n\rTEST, SETUP() ");
}

void loop() {
//Serial.println(".");
  if ( Serial.available())
  {
    receiv = Serial.read();
    if (receiv >= cmdCH && receiv <= cmdMR)
    {
      delay(25); //wait for new char - value of command
      receiv2 = Serial.read();
           if(false)
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
      }    
      else if (receiv == cmdCV) // servo Vertical
      {
        servo206 = receiv2;
        camera_V.write(servo206);
      }
      else if (receiv == cmdML) // motor L
      {
        servo209 = receiv2;
        motor_L.write(servo209);
      }
      else if (receiv == cmdMR) // motor R
      {
        servo210 = receiv2;
        motor_R.write(servo210);
      }
      else
      {
     //   Serial.print("ERR, bad command");
      }
    //  Serial.println(".");
    }
  }
}
