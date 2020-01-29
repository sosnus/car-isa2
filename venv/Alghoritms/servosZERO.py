import time
from imutils.video import VideoStream
import serial
import numpy as np
import cv2
import myserial

myserial.send(sName = myserial.myservo['cam_H'],sVal = 90)
myserial.send(sName = myserial.myservo['cam_V'],sVal = 90)
myserial.send(sName = myserial.myservo['motor_R'],sVal = 90)
myserial.send(sName = myserial.myservo['motor_L'],sVal = 90)

time.sleep(10)