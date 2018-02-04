# uniform color; cycle through hue
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

import time
from colorsys import hsv_to_rgb
from serial import Serial
from strip import write_led_strip


DISP_LENGTH = 8
PORT = 'put your serial port here!'


BRIGHTNESS = 0.1
SATURATION = 1.0
STEP_DEGREE = 1



with Serial(PORT, 115200, timeout=1) as ser:
    deg = 0

    while True:
        try:
            c = hsv_to_rgb(deg/360,SATURATION,BRIGHTNESS)
            write_led_strip(ser, [c]*DISP_LENGTH)

            print('hue = {:5.1f} deg'.format(deg))

            deg += STEP_DEGREE
            deg %= 360

            time.sleep(0.01)
        except KeyboardInterrupt:
            break
