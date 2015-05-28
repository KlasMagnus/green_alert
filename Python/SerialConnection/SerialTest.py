__author__ = 'Magnus Johansson'
#opens serial connection on COM4 and prints received lines
import serial
import time
ser = serial.Serial('\\.\COM4', 9600, timeout=0)    #under Linux port will be something like '/dev/ttyACM0'
while 1:
    try:
        line = ser.readline()
        print(line)
        time.sleep(1)
    except ser.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)

