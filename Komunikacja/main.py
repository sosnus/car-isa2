import myserial
import time
a = 60
print("[INIT] main.py")
while 1:
    myserial.setServo(sVal = a)
    myserial.setServo(sName = 'cam_V',sVal = a)
    time.sleep(0.05)
    a = a + 1
    if a == 120:
        a = 60
#     myserial.setServo(sVal = 90)
#     time.sleep(3)
#     myserial.setServo(sVal = 120)
#     time.sleep(3)
#     myserial.setServo(sName = 'cam_V',sVal = 90)
    
#     time.sleep(5)
#     myserial.setServo(sVal = 120)
#     time.sleep(5)
    
#     myserial.stopWheels()
#     time.sleep(3)
#     myserial.setWheels(diff = 10, speed = 0)
#     time.sleep(3)
#     myserial.setWheels(diff = 0, speed = 0)
#     time.sleep(3)
#     myserial.setWheels(diff = 0, speed = 20)
#     time.sleep(3)
#     myserial.stopWheels()
#     time.sleep(3)


while 1:
    
    myserial.send(sName = myserial.myservo['motor_R'],sVal = 89)
    myserial.send(sName = myserial.myservo['motor_L'],sVal = 88)
    myserial.receive()
    time.sleep(1)
    temp1 = temp1+1


while 1:
    myserial.send(sName = myserial.myservo['cam_H'],sVal = 120)
    myserial.send(sName = myserial.myservo['cam_V'],sVal = 120)
    myserial.receive()
    time.sleep(2)
    myserial.send(sName = myserial.myservo['cam_H'],sVal = 1)
    myserial.send(sName = myserial.myservo['cam_V'],sVal = 1)
    myserial.receive()
    time.sleep(2)