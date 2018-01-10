# uniform random color at random interval
# Stanley H.I. Lio
import time, math
from random import random,randint
from colorsys import hsv_to_rgb
from strip import Strip


DISP_LENGTH = 8
PORT = 'COM43'

with Strip(DISP_LENGTH,PORT) as strip:
    while True:
        try:
            c = hsv_to_rgb(random(),1,0.05)
            for k in range(DISP_LENGTH):
                strip.set_bit(k,c)
                time.sleep(0.01*random())
            time.sleep(0.2*random())
        except KeyboardInterrupt:
            break
