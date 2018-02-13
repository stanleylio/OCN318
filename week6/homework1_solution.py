# Homework 1 - Plot a CSV from grogdata.soest.hawaii.edu
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import matplotlib.pyplot as plt


whateveryouwant = open('makaipier,node-010,d2w.csv')
lines = whateveryouwant.readlines()
whateveryouwant.close()

# "lines" is a list of strings

X = []
Y = []
for agiantstring in lines[1:]:      # skip the first line
    alist = agiantstring.split(',')
    x = float(alist[0])
    y = float(alist[1])
    
    X.append(x)
    Y.append(y)
    print(X)

# X, Y, both are lists


plt.figure()
plt.plot(X, Y, '.-')
plt.savefig('hw1.png')
plt.
