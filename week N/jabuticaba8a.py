# Visualization
# "If people sat outside and looked at the stars each night, I'll bet they'd live a lot differently."
#
# Prereq:
#   built-in functions: list(), open(), float()
#   modules: matplotlib, request
# Nice to know: List Comprehension
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18



# use someone else's library
import matplotlib.pyplot as plt

plt.xkcd()

# plot the third column
D = []
for line in open('serial_log.txt'):
    line = line.strip().split(',')
    if len(line) != 10:
        continue    # NEW - https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
    D.append(float(line[2]))

plt.figure()
plt.plot(D)
plt.show()





# remove any sub-zero readings
D = [d if d >= 0 else float('nan') for d in D]
plt.figure()
plt.plot(D, '.', label='Temperature')
plt.xlabel('sample index')
plt.ylabel('Deg.C')
plt.title('Temperature')
plt.grid(True)
#plt.savefig('haha.png')    # enable this to save the plot
plt.show()
