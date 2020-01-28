#!/usr/bin/env python
import time
import serial
#Class myserial:
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

myservo =  {
    "cam_H": 209,
    "cam_V": 210,
    "motor_L": 211,
    "motor_R": 212
    
}

# def myserial():
print("[INIT] myserial.py")
    
def send(sName = '0xd1', sVal = '0x64'):
    print('send: ', end= ' ')
    print(sName, end = '=' )
    print(sVal)
    ser.write(bytes([sName]))
    ser.write(bytes([sVal]))
 #   ser.write(str.encode('\r\n'))
    
def receive():
    x=ser.readline()
    print(x)
    while x != b'':
        x=ser.readline()
        print(x)
    print("exit receive loop")
        
        
#while 1:
#    x=ser.readline()
#    print(x)
#    ser.write(str.encode('0xd1'))
#    ser.write(str.encode('0x64'))
#    ser.write(str.encode('\r\n'))
#   x=ser.readline()
 #   print(x)
  #  time.sleep(2)
  #  x=ser.readline()
#    print(x)
 #   ser.write(str.encode('0xd1'))
 #   ser.write(str.encode('0x64'))
 #   ser.write(str.encode('\r\n'))
 #   x=ser.readline()
 #   print(x)
 #   x=ser.readline()
 #   print(x)
 #   time.sleep(2)
 #   x=ser.readline()
 #   print(x)
 #   x=ser.readline()
 #   print(x)
 #   time.sleep(2)
 #   x=ser.readline()
 #   print(x)
#    port='/dev/ttyUSB0',
