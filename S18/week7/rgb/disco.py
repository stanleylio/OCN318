# random pixel with random colors at random time
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

import time
from random import random, randint
from colorsys import hsv_to_rgb
from strip import Strip


DISP_LENGTH = 8


with Strip(DISP_LENGTH, input('PORT=')) as strip:
    while True:
        try:
#            strip.blink(randint(0,DISP_LENGTH - 1),duration=random()/20,dutycycle=random(),\
#                  color=hsv_to_rgb(random(),1,random()/20))

            strip.set_bit(randint(0, DISP_LENGTH - 1), hsv_to_rgb(random(), 1, random()/10))
            strip.clear_bit(randint(0, DISP_LENGTH - 1))
            strip.clear_bit(randint(0, DISP_LENGTH - 1))
            #strip.clear_bit(randint(0, DISP_LENGTH - 1))
            #strip.clear_bit(randint(0, DISP_LENGTH - 1))
        except KeyboardInterrupt:
            break
