#include <Servo.h>


Servo camera_H;
Servo camera_V;

 Servo motor_L;
 Servo motor_R;

uint8_t servo205 = 90;
uint8_t servo206 = 90;
uint8_t servo209 = 90;
uint8_t servo210 = 90;



int receiv = 90;

uint8_t receiv2 = 90;

void setup() {
  // put your setup code here, to run once:

camera_H.attach(5);
camera_V.attach(6);

 motor_L.attach(9);
 motor_R.attach(10);

 
  Serial.begin(9600);

  
      Serial.print("\n\rTEST, SETUP() ");
}

void loop() {

  
//
//      camera_H.write(servo205);  
//      camera_V.write(servo206);   
//      motor_L.write(servo209);   
//      motor_R.write(servo210);
//      
      delay(2000); 

        Serial.print("new: ");
        Serial.println(Serial.available());


//      camera_H.write(20);  
//      delay(2000); 
//      camera_V.write(20);   
//      delay(2000); 
//      motor_L.write(70);   
//      delay(2000); 
//      motor_R.write(110);
//      delay(2000); 
//
//      
//      camera_H.write(160);  
//      delay(2000); 
//      camera_V.write(160);   
//      delay(2000); 
//      motor_L.write(110);   
//      delay(2000); 
//      motor_R.write(70);
//      delay(2000); 
//
//
//
//      motor_L.write(90);   
//      delay(2000); 
//      motor_R.write(90);
//      delay(2000); 
//
//      

  
 if ( Serial.available())
  {
    receiv = Serial.read();
    if (receiv > 200 && receiv < 255)
    {
      // NEW COMMAND
      Serial.print("\n\rReveive: ");
      Serial.print(receiv);
      Serial.print("=" );
      delay(50); //wait for new char - value of command
              receiv2 = Serial.read();
        Serial.println(receiv2);
        
      if (receiv == 205) // servoDrop
      {
        servo205 = receiv2;
      }
      else if (receiv == 206) // servoParachute
      {
        
        servo206 = receiv2;
      }
      else if (receiv == 209) // servoParachute
      {
        
        servo209 = receiv2;
      }
      else if (receiv == 210) // servoParachute
      {
        
        servo210 = receiv2;
      }
      else
      {
        Serial.println("ERR, bad command");
      }
      
        Serial.println("!");
    }
  }
}
