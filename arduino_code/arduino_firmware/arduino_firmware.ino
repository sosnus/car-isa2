#include <Servo.h>

uint8_t values[13] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};


Servo camV;
Servo camH;
Servo wheels;

int intFromSerial = 3;

enum channel {SharpL = 0,  SharpC,  SharpR,  Baterry,  Wheels,  Motor,  Motor2,  Dir1,  Dir2,  CamH,  CamV};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("SharpL,  SharpC,  SharpR,  Baterry,  Wheels,  Motor,  Motor2,  Dir1,  Dir2,  CamH,  CamV");
}

int serialToArray()
{

  delay(100);
  Serial.print("New bytes: ");
  Serial.println(Serial.available());
  for (int i = 0; i < 12; i++)
  {
    intFromSerial = Serial.parseInt();
    if (i < 3)
    {
      if ((i + 256) == intFromSerial)
        Serial.println("checksum ok!");
      else
      {
        
        Serial.println("checksum BAD!");
        return 1;
      }
    }
    else
    {
      values[i] = intFromSerial;
    }

  }
  return 0;
}

void loop() {
  // read from hardware
  values[SharpL] = analogRead(A0);
  values[SharpC] = analogRead(A1);
  values[SharpR] = analogRead(A2);
  values[Baterry] = analogRead(A3);

  if (Serial.available())
  {
    serialToArray();
  }

  for (uint8_t i = 0; i < 12; i++)
  {
    Serial.print(values[i]);
    Serial.print('\t');
  }
  Serial.println(' ');

  delay(2500);
}
