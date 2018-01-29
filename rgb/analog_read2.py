# Plot a single analog voltage channel
#
# Quite a few things should be improved. Here's a few:
#   What's the X axis? An axis of time would be more meaningful than an axis of sample index.
#   What's the sampling rate? Is it stable? How much does it fluctuate?
#   Can we store the data as well?
#   Multiple channels on the same graph?
#   Error handling: what happen if/when float() fails? (it raises a ValueError)
#   How does this compare to matplotlib.animation? https://matplotlib.org/api/animation_api.html
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

import time, math
from serial import Serial
from strip import write_led_strip
import matplotlib.pyplot as plt
plt.ion()


PORT = '/dev/ttyACM0'
N = 100
CH = 1


#plt.figure()
D = []
with Serial(PORT, 115200, timeout=1) as ser:
    
    while True:

        ser.write('read_a{}\n'.format(CH).encode())
        v = ser.readline()
        if len(v):      # don't do anything if we didn't get a response
            D.append(float(v))
            plt.gcf().clear()
            plt.plot(D, 'r')
            plt.grid(True)
            plt.ylabel('Volt')
            # fixed y limits (valid analog input range is [0V, 5V])
            #plt.ylim([0, 5])

        # give the plot a chance to update
        plt.pause(0.001)

        # trim old samples
        while len(D) > N:
            D.pop(0)

plt.show()
plt.ioff()
