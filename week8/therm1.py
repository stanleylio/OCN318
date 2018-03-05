# playing with thermistors
#
# From the datasheet we get the table of temperature-resistance pairs:
# https://www.murata.com/~/media/webrenewal/support/library/catalog/products/thermistor/ntc/r44e.ashx
#
# Given how we wired the sensor (voltage divider with thermistor on top going into ADC), we seek the function
#   temperature = f(voltage)
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import matplotlib.pyplot as plt
import numpy as np


# copy and paste from datasheet:
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

# two quirks in the original table: 0 and 5 Deg.C ended up on the same line (fix that manually);
# it uses '–' (unicode) instead of '-'. Fixed with a simple .replace().

# parse the table into a list of temperature and a list of resistance:
table = table.strip().replace('–', '-').split('\n')
t = table[0:int(len(table)/2)]
r = table[int(len(table)/2):]
t = [float(tt) for tt in t]
r = [float(rr)*1e3 for rr in r]
t = np.array(t)
r = np.array(r)
#print(len(t))
#print(len(r))

# so at this point we have two lists of equal size, t and r, each is a list of floats.

# we know what the voltage reading should be given the resistance of the thermistor
# from there we get a list of voltage
v = 10e3/(r + 10e3)*5

# so at this point we have two lists, v and t: v is the voltage we expect given a temperature t
# we no longer need r.

# find the polynomial best-fit from v (voltage) to t (temperature):
n = 8
p = np.polyfit(v, t, n)
print('The polynomial:')
print(p)

# ok so at this point we got the polynomial that maps v to t. How about we wrap
# that in a function so we can reuse it later? i.e., temperature = f(voltage)?

# let's call it v2t: "voltage to temperature"
def v2t(v):
    return np.polyval(p, v)


# let's test it with a value I got from the sensor:
adc = 2.334
print('Temperature is {:.2f} Deg.C when voltage is {:.3f} V'.format(v2t(adc), adc))
# 21.7 Deg.C in my office... sounds reasonable.



if '__main__' == __name__:
    
    # to see how good the fit is visually, we sample the polynomial at 100 evenly-spaced points from 0V to 5V:
    x = np.linspace(0, 5, 100)
    y = np.polyval(p, x)

    plt.figure()
    plt.plot(v, t, '.', label='table')
    plt.plot(x, y, 'r-', label='{}-th degree best-fit'.format(n), alpha=0.5)
    plt.title('Voltage-temperature {}-th deg. best-fit'.format(n))
    plt.xlabel('Voltage, V')
    plt.ylabel('Temperature, Deg.C')
    plt.grid(True)
    plt.legend()

    plt.show()
