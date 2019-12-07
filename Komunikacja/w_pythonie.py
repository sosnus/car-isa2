import serial
ser = serial.Serial('/dev/ttyS0',9600)
time.sleep(5)
ser.write(str.encode('5'))
