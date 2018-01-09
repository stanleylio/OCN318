#!/usr/bin/python3
# single pixel fixed color running light
# Stanley H.I. Lio
import time, math
from strip import Strip


DISP_LENGTH = 16
PORT = 'COM10'

with Strip(DISP_LENGTH,PORT) as strip:
    while True:
        try:
            for k in range(DISP_LENGTH):
                strip.set_bit(k,(0,.2,.2))
                time.sleep(0.01)
                strip.clear_bit(k)
        except KeyboardInterrupt:
            break
