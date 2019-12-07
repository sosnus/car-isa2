#include <Servo.h>

uint8_t values[13] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

Servo camV;
Servo camH;
Servo wheels;

enum channel {SharpL = 0,  SharpC,  SharpR,  Baterry,  Wheels,  Motor,  Motor2,  Dir1,  Dir2,  CamH,  CamV};

void setup() {
  Serial.begin(115200);
  Serial.println("SharpL,  SharpC,  SharpR,  Baterry,  Wheels,  Motor,  Motor2,  Dir1,  Dir2,  CamH,  CamV");
}

void serialPrintCurrentArray()
{
  for (uint8_t i = 0; i < 12; i++)
  {
    Serial.print(values[i]);
    Serial.print('\t');
  }
  Serial.println(' ');
}

int serialToArray()
{
  if (Serial.available())
  {
    int intFromSerial = 3;
    delay(100);
    for (int i = 0; i < 12; i++)
    {
      intFromSerial = Serial.parseInt();
      if (i < 3)
      {
        if ((i + 256) != intFromSerial)
        {
          return 1; // bad checksum
        }
      }
      else
      {
        values[i] = intFromSerial;
      }
    }
    return 0;
  }
  else
  {
    return 2; // no data (Serial.available())
  }
}

void analogToArray()
{
  values[SharpL] = analogRead(A0);
  values[SharpC] = analogRead(A1);
  values[SharpR] = analogRead(A2);
  values[Baterry] = analogRead(A3);
}

void loop() {
  analogToArray();
  Serial.print("serialToArray() status: ");
  Serial.println(serialToArray());
  serialPrintCurrentArray();
  delay(2500);
}
