import serial
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.write(str.encode('2'))