import myserial
import time


# myserial.myservo['cam_H']
# myserial.myservo['cam_V']
# myserial.myservo['motor_L']
# myserial.myservo['motor_R']

# sVal must be between 1 and 180


print("[INIT] main.py")
temp1 = 80
while 1:
    myserial.stopWheels()
    time.sleep(3)
    myserial.setWheels(diff = 10, speed = 0)
    time.sleep(3)
    myserial.setWheels(diff = 0, speed = 0)
    time.sleep(3)
    myserial.setWheels(diff = 0, speed = 20)
    time.sleep(3)
    myserial.stopWheels()
    time.sleep(3)


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