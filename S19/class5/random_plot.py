import time
from random import random
import numpy as np
import matplotlib.pyplot as plt
plt.ion()


D = []
while True:
    D.append(random())

    plt.clf()
    plt.plot(D, 'b')
    plt.grid(True)
    plt.pause(0.05)

    while len(D) > 100:
        D.pop(0)

plt.ioff()
