# uniform random color at random interval
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

import time
from random import random
from colorsys import hsv_to_rgb
from serial import Serial
from strip import write_led_strip


DISP_LENGTH = 8


with Serial(input('PORT='), 115200, timeout=1) as ser:
    while True:
        try:
            c = hsv_to_rgb(random(), 1, 0.05)
            write_led_strip(ser, [c]*DISP_LENGTH)
            time.sleep(0.3*random())
        except KeyboardInterrupt:
            break
