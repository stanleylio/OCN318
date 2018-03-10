import sys
sys.path.append('../week7/rgb')
from serial import Serial
from strip import write_led_strip


ser = Serial('COM6', 115200, timeout=1)

while True:
    res = input()
    if 'r' == res:
        write_led_strip(ser, [[0.5,0,0]]*8)
    if 'g' == res:
        write_led_strip(ser, [[0,0.5,0]]*8)
    if 'b' == res:
        write_led_strip(ser, [[0,0,0.5]]*8)

ser.close()

