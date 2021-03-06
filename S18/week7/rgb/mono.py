# set all pixels to cyan then exit
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

from serial import Serial
from strip import write_led_strip


DISP_LENGTH = 8


with Serial(input('PORT='), 115200, timeout=1) as ser:
    color = [(0, 0.1, 0.07)]
    write_led_strip(ser, color*DISP_LENGTH)

print('done.')
