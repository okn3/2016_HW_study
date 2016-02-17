# -*- coding: utf-8 -*-
import serial
import time

port = "/dev/tty.usbmodem1421"
ser = serial.Serial(port, 9600, timeout=1)

# LED sample ----------------------------------
def on_off():
    while True:
        num = raw_input("1:on 0:off \n__>")
        ser.write(num)

def blink():
    while True:
        ser.write('1')
        time.sleep(0.3)
        ser.write('0')
        time.sleep(0.3)


# add your function

# Full Color LED sample -------------------------
def fc_control():
    while True:
        color = input("0:none 1:red 2:green 3:blue \n__>")
        if color >= 0 and color <= 3:
            ser.write(str(color))
        else:
            print "input error"

def main():
#        blink()
        on_off()
#    fc_control()

if __name__ == '__main__':
    main()
