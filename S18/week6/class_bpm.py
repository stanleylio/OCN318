# Beat-Per-Minute estimation demo
# (live code from class)
# See bpm.py for a more complete version.
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import time
import numpy as np
import matplotlib.pyplot as plt


T = []
for i in range(10):
    try:
        input('Hit ENTER when you are ready:')
        t = time.time()
        T.append(t)
        
        print(60*1/np.mean(np.diff(T)))
    except KeyboardInterrupt:
        break


plt.figure()
plt.plot(T, '.')

plt.figure()
plt.plot(np.diff(T), '.')

plt.figure()
plt.hist(np.diff(T))

plt.show()
