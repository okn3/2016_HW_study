import serial
import time
ser = serial.Serial("/dev/tty.usbmodem1421",9600)

print "reading..."
while True:
    time.sleep(1)
    r_char = ser.read()
#    r_str = ser.read(2)
#    r_line = ser.readline()

    print r_char

ser.close()
