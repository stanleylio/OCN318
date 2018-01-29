# Control flow - if, for, while
# "... one folk in the road leads to honesty, another path leads the path of love."
#
# See also (advanced): built-in functions range(), zip()
#
# Important and very useful, but I don't expect you to know them until next class.
# https://docs.python.org/3/tutorial/datastructures.html#looping-techniques
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18



# IF
if True:
    print('do something')
else:
    print('do something else')

# combined with the "in" operator
# memorize this one. we use it a lot.
if 'proof' in 'the puddin':
    print('yup')
else:
    print('nope')

# our old friend the floats.
if 0.1 + 0.1 + 0.1 == 0.3:
    print('I was playing with my phone')
else:
    print('I paid attention')






# FOR
# do something to each and every item in order
for s in ['call', 'write']:
    print('you never {}'.format(s))

# repeat something multiple times
for i in range(5):
    print(i)
# Observations: i starts from 0; i never reaches 5; loop ran 5 times nonetheless





A = ['Born', 'Christened', 'Married', 'Took ill', 'Grew Worse', 'Died', 'Buried']
B = ['a Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# note: "list()" is for illustrative purpose. Look up "iterable" (advanced) if you want to learn more.
for a,b in list(zip(A, B)):
    print(a + ' on ' + b)





# WHILE
# "repeat something as long as condition is True"
#while True:
#    print('broken record')
# Ctrl + C to break





energy = 10000
while energy > 9000:
    print("{}: IT'S OVER NINE THOUSAND!".format(energy))
    energy = energy - 200



# you can stop the loop midway:
for i in range(10):
    print(i)
    if i > 5:       # note the 6. why?
        break





# "What's the point of all this?"
# Example 1
tags = ['timestamp', 'temperature', 'pressure']
readings = ['2018-01-26 03:08:09', 25.00, 101.325]
d = dict(zip(tags, readings))
# now you can refer to a reading by its name
# if you pass this to another program / person, they would know what the values mean because they are all named
print('Temperature = {} Deg.C, pressure = {} kPa'.format(d['temperature'], d['pressure']))




# Example 2
reading = {'timestamp':'2018-01-26 03:08:09', 'temperature':25.00, 'pressure':101.325}
calibration_factors = {'temperature':1.038, 'pressure':1.000083}
# for "something" in "some collection" - we see this pattern a lot
for key in calibration_factors:
    print(reading[key]*calibration_factors[key])


# Reading:
# read the sections on int(), float(), sum(), bytearray()
#https://docs.python.org/3/library/functions.html
