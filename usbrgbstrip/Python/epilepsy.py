# uniform random color at random interval
# Stanley H.I. Lio
import time, math
from random import random,randint
from colorsys import hsv_to_rgb
from strip import Strip


DISP_LENGTH = 16
PORT = 'COM10'

with Strip(DISP_LENGTH,PORT) as strip:
    while True:
        try:
            c = hsv_to_rgb(random(),1,random()**2)
            for k in range(DISP_LENGTH):
                strip.set_bit(k,c)
                time.sleep(0.01*random())
            time.sleep(0.2*random())
        except KeyboardInterrupt:
            break
