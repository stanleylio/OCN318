# Single-pixel chase light
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

import time, math
from strip import Strip


DISP_LENGTH = 8


with Strip(DISP_LENGTH, input('PORT=')) as strip:
    while True:
        try:
            for k in range(DISP_LENGTH):
                strip.set_bit(k,(0, .2, .2))
                strip.set_bit(DISP_LENGTH - k - 1,(.1, .1, 0))
                time.sleep(0.01)
                strip.clear_bit(k)
                strip.clear_bit(DISP_LENGTH - k - 1)
        except KeyboardInterrupt:
            break
