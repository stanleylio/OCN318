# Even more plotting
#
# https://matplotlib.org/gallery.html
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

import time
from random import random
import numpy as np
import matplotlib.pyplot as plt
plt.ion()


D = []
for i in range(100):
    
    D.append(random())

    plt.clf()
    plt.plot(D, 'r')
    plt.grid(True)
    plt.pause(0.05)


plt.ioff()
