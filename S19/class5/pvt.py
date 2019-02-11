# class demo - plot PvT
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import matplotlib.pyplot as plt
import numpy as np


#plt.xkcd()


# plot the third column
T = []
P = []
for line in open('serial_log.txt'):
    line = line.strip().split(',')
    if len(line) != 10:
        continue
    T.append(float(line[2]))
    P.append(float(line[3]))
    

# replace bad reading(s) with the sample mean
sample_mean = np.mean(T)
T = [t if t >= 0 else sample_mean for t in T]

# 
T = np.array(T)
P = np.array(P)

# normalize...
#T = T/np.max(T)
#P = P/np.max(P)

# ... or ZNCC?
T = (T - np.mean(T))/np.std(T)
P = (P - np.mean(P))/np.std(P)

print(np.corrcoef(T, P))

plt.figure()
plt.plot(T, P, '.')
plt.xlabel('Temperature (normalized)')
plt.ylabel('Pressure (normalized)')
plt.title('Temperature vs. Pressure')
plt.grid(True)
plt.axis('equal')
plt.savefig('tvp.png')
plt.show()
