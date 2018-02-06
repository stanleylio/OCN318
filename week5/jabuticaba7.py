# Common use case - File IO
# "Everything not saved will be lost."
#
# Prereq:
#   string operations: split(), strip(), format(), join()
#   list operations: append()
#   built-in functions: len(), open()
#
# Reading:
#   open()
#       https://docs.python.org/3/library/functions.html#open
#   string.strip()
#       https://stackoverflow.com/a/13013812/4570438
#
# Advanced topic: the "with" construct
# https://docs.python.org/3/reference/compound_stmts.html#with
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18



# to write to a file:
f = open('offshore_assets.txt', 'w')    # homework: look up the 'r' and 'a' options
f.write('squirrel tail')
f.write('basilisk hide')
f.write('kikimore claw')
f.write('may contain peanut')
f.close()
# hint: this is a new line character: '\n'
# Exercise: put the strings on separate lines


# to read from a file:
f = open('offshore_assets.txt')
while True:
    line = f.readline()
    if len(line) > 0:
        print(line)
    else:
        break
f.close()

# more succinctly,
for line in open('offshore_assets.txt'):
    print(line)






# Exercise: copy THE THIRD column from serial_log.txt into temperature.csv
D = []
for line in open('serial_log.txt'):
    line = line.strip().split(',')
    if 10 == len(line):
        D.append(line[2])
print(len(D))
print(D[:10])

f = open('temperature.csv', 'w')
for d in D:
    f.write('{}\n'.format(d))
f.close()




# Homework: extract the FIRST FOUR columns from serial_log.txt and place them in output1.csv
# Hint: you might need the join() method for strings. Try this: ','.join(['a', 'b', 'c'])




# Challenge: merge the first two columns by adding them, write it and the second and thrid columns to output2.csv
# Like so:
# INPUT:
'''
256,0,24.525,103.70,251,270,1382,1573,582,2215
256,20,24.559,103.63,252,272,1381,1570,581,2212
256,40,24.547,103.60,252,272,1380,1569,580,2210
256,60,24.539,103.72,252,271,1379,1569,579,2208
...
'''
# OUTPUT:
'''
256,24.525,103.70
276,24.559,103.63
296,24.547,103.60
316,24.539,103.72
...
'''
# (the first and second columns are index. third, temperature, and fourth, pressure in kPa.)
