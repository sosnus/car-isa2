#include <Servo.h>


Servo camera_H;
Servo camera_V;

 Servo motor_L;
 Servo motor_R;

void setup() {
  // put your setup code here, to run once:

camera_H.attach(5);
camera_V.attach(6);

 motor_L.attach(9);
 motor_R.attach(10);
}

void loop() {
      camera_H.write(20);  
      delay(2000); 
      camera_V.write(20);   
      delay(2000); 
      motor_L.write(70);   
      delay(2000); 
      motor_R.write(110);
      delay(2000); 

      
      camera_H.write(160);  
      delay(2000); 
      camera_V.write(160);   
      delay(2000); 
      motor_L.write(110);   
      delay(2000); 
      motor_R.write(70);
      delay(2000); 



      motor_L.write(90);   
      delay(2000); 
      motor_R.write(90);
      delay(2000); 

      

  


         
    delay(15);  
  // put your main code here, to run repeatedly:

}
