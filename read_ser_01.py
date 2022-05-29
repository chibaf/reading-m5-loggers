import serial, sys
import syslog
import time

#The following line is for serial over GPIO
port = sys.argv[1]
speed = sys.argv[2]

ser = serial.Serial(port,speed)

while True:
    # Serial read section
    line = ser.readline()
    line2=line.strip().decode('utf-8')
    data = [str(val) for val in line2.split(",")]
    print ("data array from arduino: ")
    print (data)
exit()