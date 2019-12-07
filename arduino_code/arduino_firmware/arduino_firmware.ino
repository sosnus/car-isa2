
uint8_t values[13]= {0,1,2,3,4,5,6,7,8,9,10,11,12};

enum channel {SHARP_L = 0,  SHARP_C,  SHARP_R,  BATERRY,  Wheels,  Motor,  Motor2,  Dir1,  Dir2,  CAM_H,  CAM_V};

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
Serial.println("Arduino ISA test...");
}

void loop() {
  values[SHARP_L] = analogRead(A0);
  values[SHARP_C] = analogRead(A1);
  values[SHARP_R] = analogRead(A2);
  values[BATERRY] = analogRead(A3);
  for(uint8_t i = 0; i<12; i++)
  {
    Serial.print(values[i]);
    Serial.print('\t');
  }
    Serial.println(' ');
  
  delay(1000);
  // put your main code here, to run repeatedly:

}
