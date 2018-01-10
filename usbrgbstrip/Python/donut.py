#!/usr/bin/python3
# Stanley H.I. Lio
import time, math
from strip import Strip


DISP_LENGTH = 8
PORT = 'COM10'

with Strip(DISP_LENGTH,PORT) as strip:
    r = [(1,0,0)]*DISP_LENGTH
    b = [(0,0,1)]*DISP_LENGTH
    off = [(0,0,0)]*DISP_LENGTH
    while True:
        try:
            for i in range(4):
                strip.set_all(r)
                time.sleep(0.05)
                strip.set_all(off)
                time.sleep(0.05)
            
            time.sleep(0.1)

            for i in range(4):
                strip.set_all(b)
                time.sleep(0.05)
                strip.set_all(off)
                time.sleep(0.05)

            time.sleep(0.2)
        except KeyboardInterrupt:
            break
