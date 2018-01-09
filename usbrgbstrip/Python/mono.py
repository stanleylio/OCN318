#!/usr/bin/python3
# set all pixels to cyan then exit
from strip import Strip


DISP_LENGTH = 16

strip = Strip(DISP_LENGTH,'COM10')

color = (0,0.1,0.07)
for k in range(DISP_LENGTH):
    strip.set_bit(k,color)

print('done.')
