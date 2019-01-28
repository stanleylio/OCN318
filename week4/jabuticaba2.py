# Data Type: STRING
#
# Reading: https://docs.python.org/3.6/library/string.html
# Particularly, format(), strip(), split()
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18, S19


# STRING
# These are strings:
# single-quote
'7.62 NATO'
# double-quote
"weapon of mass instruction"
# single-quote multi-line
'''multi-
line'''
# double-quote multi-line
"""multi-
line"""



# conversion from string to int and float
print(type('96822'))
print(type(int('96822')))
print(type('   299792.458     '))
print(type(float('   299792.458     ')))



# replacement
a = "let's eat grandma"
# works
print(a.replace('eat','eat,'))
# also works
print(a.replace('at','at,'))
# no longer. why?
print(a.replace('t','t,'))
readings = '250.6uM, 252.9uM, 260.1uM'
print(readings.replace('uM', ''))





# concatenation
s = 'laughter'
print(s + 's')
print('s' + s)




# the format() operation ("fill in the blank")
# by position
a = "if you don't do {} I {}"
print(a.format('homework', 'kill this kitten'))
# by name
print('{x}, {x} everywhere'.format(x='cactus'))




# indexing ("slice and dice")
#   index starts with 0
#   item pointed by the second index is not included
a = "discouraged"
print(a[6:10])
# count backward from the end with negative index
# if begin/end is not specified, it's taken to the begin/end of the string
print(a[-4:])

# (optional) reverse a string
print('maps'[::-1])





# the split() operation
a = '1516969860,25.738,103.225,7603'
print(a.split(','))
# that gives you a LIST of STRINGs (more on List later):
print(type(a.split(',')))
# also notice that the original variable is not modified:
print(a)





# membership: the "in" operator
thebox = 'what\'s in the box'
print('head' in thebox)
print('hat' in thebox)




# the built-in len() function
a = "discouraged"
# count the number of characters (including spaces and punctuations, but NOT the surrounding quotes)
print(len(a))
b = 'truth, justice, and the American way'
# count the number of words
print(len(a.split(' ')))
# what does this count?
print(len(a.split(',')))






# counting occurrence
a = 'There are old pilots and there are bold pilots, but there no old, bold pilots.'
print(a.count('pilots'))






# also notice this does nothing:
"Come watch TV?"
# Literals don't do anything on their own (except in REPL), so you can temporarily
# disable a block of code by surrounding it in quotes:
"""
print('this does not print')
#this whole block is ignored by Python
print('forever alone')
"""





# read the doc to see what you can do with mixing types (or just try it out)
# Python complains
#print('Trump' + 2020)
# but this is cool
print('lau'*4)






# put it all together:
a = 'cd, nano, ls, pwd, exit, apropos, sudo, cp, mv, scp'
a = a + ', ps, ssh'
a = a.split(', ')
#print(a)
# what's the output?
print(len('a'))
# what about now?
print(len(a))

# you have N seconds
import time
N = 60
for i in range(N):
    print('{} seconds left'.format(N - i))
    time.sleep(1)
print('Time\'s up.')



# Reading: string.join()
# https://www.tutorialspoint.com/python/string_join.htm
