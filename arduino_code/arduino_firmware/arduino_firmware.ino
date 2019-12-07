#include <Servo.h>

uint8_t values[13]= {0,1,2,3,4,5,6,7,8,9,10,11,12};


Servo camV; 
Servo camH; 
Servo wheels; 

enum channel {SharpL = 0,  SharpC,  SharpR,  Baterry,  Wheels,  Motor,  Motor2,  Dir1,  Dir2,  CamH,  CamV};

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
//Serial.println("Arduino ISA test...");
Serial.println("SharpL,  SharpC,  SharpR,  Baterry,  Wheels,  Motor,  Motor2,  Dir1,  Dir2,  CamH,  CamV");
}

void loop() {
  // read from hardware
  values[SharpL] = analogRead(A0);
  values[SharpC] = analogRead(A1);
  values[SharpR] = analogRead(A2);
  values[Baterry] = analogRead(A3);

  //read from serialport
  // buffer sync
  //TODO: buffer sync
  /*
  int intFromSerial = 
  do{
    
  }while
  values[Motor] = 

*/
  
  for(uint8_t i = 0; i<12; i++)
  {
    Serial.print(values[i]);
    Serial.print('\t');
  }
    Serial.println(' ');
  
  delay(250);
  // put your main code here, to run repeatedly:

}
