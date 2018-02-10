# 8-LED stick as volume display for analog voltage
#
# "As I hurtled through space, one thought kept crossing my mind - every part
# of this rocket was supplied by the lowest bidder."
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

import time, math
from serial import Serial
from strip import write_led_strip


DISP_LENGTH = 8
PORT = 'put your serial port here!'


with Serial(PORT, 115200, timeout=1) as ser:
    
    while True:

        ser.write('read_raw_a0\n'.encode())
        v = ser.readline()
        if len(v):
            v = float(v)/1024.0     # normalize v from [0,1023] to [0,1]
            #print(v)

            count = int(v*8)        # map it to an integer in [0,8]
            print('囧'*count)
            
            try:
                tmp = [(0,0,0)]*DISP_LENGTH
                for i in range(count):
                    tmp[i] = (v**3*0.3, 0, (1-v)*0.3)
                for i in range(count, DISP_LENGTH):
                    tmp[i] = (0,0,0)
                write_led_strip(ser, tmp)

                #time.sleep(0.1)
            except KeyboardInterrupt:
                break
