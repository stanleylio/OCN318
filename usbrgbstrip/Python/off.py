#!/usr/bin/python3
# turn all LEDs off
# Stanley H.I. Lio
from strip import Strip


DISP_LENGTH = 16
PORT = 'COM10'

strip = Strip(DISP_LENGTH,PORT)

color = (0,0,0)
for k in range(DISP_LENGTH):
    strip.set_bit(k,color)

print('done.')
