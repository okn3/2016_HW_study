# coding:utf-8
"""
arduinoからシリアル通信しつぶやく
"""

import serial
import time, os
ser = serial.Serial("/dev/tty.usbmodem1421",9600)

print "reading..."
while True:
    time.sleep(1)
    r_char = ser.read()
    print r_char
    if r_char == "1":
        os.system("say hoo")        

#ser.close()
