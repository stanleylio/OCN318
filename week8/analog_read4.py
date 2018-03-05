# Plot temperature readings.
#
# "In indoor farming, we see a lot of competition focus on how data will drive
# yield increases, yet they haven't figured out how to regulate air temperature
# in their facility".
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import time, math, sys
sys.path.append('../week7/rgb')
from serial import Serial
from strip import write_led_strip
import matplotlib.pyplot as plt
import numpy as np
from therm1 import v2t
plt.ion()


N = 100
CH = 0


#plt.figure()
D = []
with Serial(input('PORT='), 115200, timeout=1) as ser:
    
    while True:

        ser.write('read_raw_a{}\n'.format(CH).encode())
        v = ser.readline()
        if len(v):      # don't do anything if we didn't get a response
            print(v)
            D.append(v2t(float(v)/1024*5))
            plt.gcf().clear()
            plt.plot(D, 'r')
            plt.annotate('{:.1f} Deg.C'.format(D[-1]), (0.6*len(D), np.mean(D)), size=24)
            plt.annotate('peak {:.1f} Deg.C'.format(D[-1]), (0.6*len(D), max(D)), size=18)
            plt.grid(True)
            plt.ylabel('Deg.C')
            # fixed y limits (valid analog input range is [0V, 5V])
            #plt.ylim([0, 5])

        # give the plot a chance to update
        plt.pause(0.01)

        # trim old samples
        while len(D) > N:
            D.pop(0)

plt.show()
plt.ioff()
