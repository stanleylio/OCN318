# playing with thermistors (optional)
#
# Two things:
#   1. t-r vs. t-log(r)
#   2. voltage -> resistance -> temperature vs. voltage -> temperature
#
# https://www.murata.com/~/media/webrenewal/support/library/catalog/products/thermistor/ntc/r44e.ashx
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import matplotlib.pyplot as plt
import numpy as np


table = '''
–40
–35
–30
–25
–20
–15
–10
–5
0
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
100
105
110
115
120
125
197.388
149.395
114.345
88.381
68.915
54.166
42.889
34.196
27.445
22.165
18.010
14.720
12.099
10.000
8.309
6.939
5.824
4.911
4.160
3.539
3.024
2.593
2.233
1.929
1.673
1.455
1.270
1.112
0.976
0.860
0.759
0.673
0.598
0.532
'''


# two quirks in the original table: 0 and 5 deg ended up on the same line; it uses '–' (unicode) instead of '-'

table = table.strip().replace('–', '-').split('\n')
t = table[0:int(len(table)/2)]
r = table[int(len(table)/2):]
t = [float(tt) for tt in t]
r = [float(rr)*1e3 for rr in r]
t = np.array(t)
r = np.array(r)
print(len(t))
print(len(r))



#plt.figure()
#plt.plot(t, r, '.')
#plt.show()


# let's try brute-force
n = 8
p = np.polyfit(t, r, n)
print('brute-force:')
print(p)

x = np.linspace(min(t), max(t), 100)
y = np.polyval(p, x)

plt.figure()
plt.plot(t, r, '.', label='table')
plt.plot(x, y, 'r-', label='{}-th degree best-fit'.format(n), alpha=0.5)
plt.title('brute-force polyfit')
plt.xlabel('temperature, deg.C')
plt.ylabel('resistance, Ohm')
plt.legend()



# but that's not a very good fit...
plt.figure()
plt.plot(t, np.log(r), '.', label='ln(table)')
plt.title('but then I noticed something...')
plt.ylabel('ln(resistance)')
plt.xlabel('temperature, deg.C')
plt.annotate('log(resistance) is much more "linear"...', xy=(20, 3))
plt.legend()



# log(resistance) is much more linear. Let's fit that instead:
# don't need that high a polynomial anymore
n = 3
p = np.polyfit(t, np.log(r), n)
print('fit ln():')
print(p)

x = np.linspace(min(t), max(t), 100)
y = np.polyval(p, x)
y = np.exp(y)


plt.figure()
plt.plot(t, r, '.', label='table')
plt.plot(x, y, 'r-', label='best-fit with ln()', alpha=0.5)
plt.xlabel('temperature, deg.C')
plt.ylabel('resistance, Ohm')
plt.title('ding!')
plt.legend()




# t-r is fine with log(). what about r-t?

plt.figure()
plt.plot(np.log(r), t, '.')

p = np.polyfit(np.log(r), t, 3)

def v2r(v):
    return 10e3/v*5 - 10e3

v = 2.334
t = np.polyval(p, np.log(v2r(v)))
print('Given a voltage measurement of {:.2f} volt, temperature should be {:.2f} Deg.C'.format(v, t))



plt.show()
