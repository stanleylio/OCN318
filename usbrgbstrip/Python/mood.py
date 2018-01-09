#!/usr/bin/python3
# uniform color; cycle through hue
# Stanley H.I. Lio
import time
from serial import Serial
from colorsys import hsv_to_rgb
from strip import Strip


DISP_LENGTH = 16
BRIGHTNESS = 0.1
SATURATION = 1.0
STEP_DEGREE = 5
PORT = 'COM10'



if '__main__' == __name__:
    with Strip(DISP_LENGTH,PORT) as strip:

        deg = 0

        while True:
            try:
                c = hsv_to_rgb(deg/360,SATURATION,BRIGHTNESS)

                #strip.set_bit(0,c)

                for k in range(DISP_LENGTH):
                    strip.set_bit(k,c)
                
                print('hue = {:5.1f} deg'.format(deg))

                deg += STEP_DEGREE
                deg %= 360

                #time.sleep(0.01)
            except KeyboardInterrupt:
                break
