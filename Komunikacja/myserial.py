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

offset_l = -1
offset_r = -1

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
    
def setWheels(diff = 0, speed = 0):
    left = (90 + offset_l) + diff + speed
    right = (90 + offset_r) + diff - speed
    ser.write(bytes([myservo["motor_L"]]))
    ser.write(bytes([left]))
    ser.write(bytes([myservo["motor_R"]]))
    ser.write(bytes([right]))
    print("set L=" , left , "  R=" , right)
    
def stopWheels():
    print("STOP MOTORS") 
    left = (90 + offset_l)
    right = (90 + offset_r)
    ser.write(bytes([myservo["motor_L"]]))
    ser.write(bytes([left]))
    ser.write(bytes([myservo["motor_R"]]))
    ser.write(bytes([right]))
    print("set L=" , left , "  R=" , right)

def setServo(sName = 'cam_H',sVal = 90):
    ser.write(bytes([myservo[sName]]))
    ser.write(bytes([sVal]))
   # receive()
    
def goToBall(ball_x = 0, ball_y = 0, ball_size = 10):
    #ball_x <-100;100> ball_size <0,200> where 200 = whole screen
    ball_y = (ball_y /2)+90
    
    
    
        
        
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
