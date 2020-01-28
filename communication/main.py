import myserial
import time


# myserial.myservo['cam_H']
# myserial.myservo['cam_V']
# myserial.myservo['motor_L']
# myserial.myservo['motor_R']

# sVal must be between 1 and 180


print("[INIT] main.py")
while 1:
    myserial.send(sName = myserial.myservo['cam_H'],sVal = 120)
    myserial.send(sName = myserial.myservo['cam_V'],sVal = 120)
    myserial.receive()
    time.sleep(2)
    myserial.send(sName = myserial.myservo['cam_H'],sVal = 1)
    myserial.send(sName = myserial.myservo['cam_V'],sVal = 1)
    myserial.receive()
    time.sleep(2)