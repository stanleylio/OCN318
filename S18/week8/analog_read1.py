# Read an ADC channel
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import time
from serial import Serial


with Serial(input('PORT='), 115200, timeout=1) as ser:
    while True:
        ser.write('read_raw_a0\n'.encode())
        a0 = float(ser.readline().decode().strip())

        print(a0)
