# Time Series example: Beat-per-minute (BPM) Estimation
#
# Run it and tap (RETURN) repeatedly.
# Hit Ctrl + C to terminate.
#
# "What do programmers actually do?"
# https://youtu.be/g4a7_HH9Wbg
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import time
import matplotlib.pyplot as plt
import numpy as np


ignore = 3


def estimate_bpm(D):
    """Given a list of timestamps, return the estimated beat-per-minute"""
    if len(D) < 2*ignore:
        return 0
    else:
        return 1/np.mean(np.diff(D))*60
    

T = []
while True:
    try:
        r = input('Hit RETURN on every beat...')
        t = time.time()
        T.append(t)
        #print(t)
        if len(T) > 2*ignore + 2:
            print('Current estimate: {:.2f} BPM, std={:.2f}, N={}'.\
                  format(estimate_bpm(T[ignore:-ignore]), np.std(1/np.diff(T[ignore:-ignore])*60), len(T)))
    except KeyboardInterrupt:
        break


#print(T)
# Calculate average period and BPM (ignore the first and last few samples)
periods = np.diff(T[ignore:-ignore])
period = np.mean(periods)
print('Got {} taps'.format(len(T)))
print('Period = {:.2f}s ({:.2f} BPM)'.format(period, 1/period*60))


plt.figure()
plt.plot(T, '.')
plt.xlabel('Sample Index')
plt.ylabel('Absolute Time (UTC)')
plt.title('Absolute Time, One dot per tap')

plt.figure()
plt.bar(range(len(periods)), periods)
plt.xlabel('Index')
plt.ylabel('Interval, seconds')
plt.title('Measured Interval')

plt.figure()
plt.hist(periods)
plt.title('Distribution of intervals')

plt.show()

# Questions:
# How many taps do you need to get N decimal places precision?
# Given that a song is X BPM, how long does it need to be to get N decimal places?
# Someone calculates the confidence interval...
