# Just run it... (update the PORT variable though.)
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

import time, math
from serial import Serial
from strip import write_led_strip


DISP_LENGTH = 8
PORT = '/dev/ttyACM0'


with Serial(PORT, 115200, timeout=1) as ser:
    r = [(1,0,0)]*DISP_LENGTH
    b = [(0,0,1)]*DISP_LENGTH
    off = [(0,0,0)]*DISP_LENGTH
    while True:
        try:
            for i in range(4):
                write_led_strip(ser, r)
                time.sleep(0.05)
                write_led_strip(ser, off)
                time.sleep(0.05)
            
            time.sleep(0.1)

            for i in range(4):
                write_led_strip(ser, b)
                time.sleep(0.05)
                write_led_strip(ser, off)
                time.sleep(0.05)

            time.sleep(0.2)
        except KeyboardInterrupt:
            break
