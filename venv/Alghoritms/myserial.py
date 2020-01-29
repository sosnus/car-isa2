#!/usr/bin/env python
import time
import serial
#Class myserial:
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

offset_l = -1
offset_r = -1

myservo =  {
    "cam_H": 205,
    "cam_V": 206,
    "motor_L": 209,
    "motor_R": 210
}

ballWidth = 10
servoX = 90
servoY = 90

# def myserial():
print("[INIT] myserial")
    
def send(sName = '0xd1', sVal = '0x64'):
    if 0:
        print('send: ', end= ' ')
        print(sName, end = '=' )
        print(sVal)
    ser.write(bytes([sName]))
    ser.write(bytes([sVal]))
#    receive()
 #   ser.write(str.encode('\r\n'))
    
def receive():
    x=ser.readline()
    print(x)
   # while x != b'':
   #     x=ser.read()
    while x != b'':
        x=ser.readline()
        print(x, end="; ")
    print("END")
    #print("exit receive loop")
    
def setWheels(diff = 0, speed = 0):
    left = (90 + offset_l) + diff + speed
    right = (90 + offset_r) + diff - speed
    ser.write(bytes([myservo["motor_L"]]))
    ser.write(bytes([left]))
    ser.write(bytes([myservo["motor_R"]]))
    ser.write(bytes([right]))
    print("set L=" , left , "  R=" , right)

def setMotors(left = 89, right = 89):
    left_t = 89 + int(left)
    right_t = 89 + int(right)
    ser.write(bytes([myservo["motor_L"]]))
    ser.write(bytes([left_t]))
    ser.write(bytes([myservo["motor_R"]]))
    ser.write(bytes([right_t]))
    print("set L=" , left_t , "  R=" , right_t, end = ">>")
#    receive()

    
def stopWheels():
    print("STOP MOTORS") 
    left = (90 + offset_l)
    right = (90 + offset_r)
    ser.write(bytes([myservo["motor_L"]]))
    ser.write(bytes([left]))
    ser.write(bytes([myservo["motor_R"]]))
    ser.write(bytes([right]))
    print("set L=" , left , "  R=" , right)
    
    
send(sName = myservo['cam_H'], sVal = 90)
send(sName = myservo['cam_V'], sVal = 90)
send(sName = myservo['motor_L'], sVal = 90)
send(sName = myservo['motor_R'], sVal = 90)




# def setServo(servo_name
    
#def goToBall(ball_x = 0, ball_y = 0, ball_size):
#    ball_y = (ball_y /2)+90
    
    #ball_x <-100;100> ball_size <0,200> where 200 = whole screen
    
    
        
        
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
