# Data Structures
# LIST, TUPLE, and DICTIONARY
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18



# bread-and-butter: LIST
# these are lists:
[]
list()      # see the color?
print(type([]))

# len() works
print(len([]))
print(len([1,2,3,4]))

# elements can be any type,
print([1, 2, 'that works', ''])
# ... including other lists
a = ['I am the first element', ['yup this works too']]
print(a)
print("That's a list of length {}".format(len(a)))
a = ['first element', [], [], [['', ['this is totally fine', ['but why would you do this', 'fiscally feasible']]]]]
print(a)
# question: what's the len() of a?
print(len(a))





# adding more elements to a list
a = [1, 2, 3, 4]
a.append('haha')
a.append('haha')
a.append('haha')
print(a)





# modify an element at a given position (index starts from 0!)
a = [1, 2, 3, 4, 5]
a[3] = 'room 101'
print(a)





# slicing also works
print(a[2:])






# append() vs. extend()
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
a.append([5, 6, 7])
b.extend([5, 6, 7])
print(a)
print(b)
print(a[4])
print(b[4])
# also check their lengths!
#print(len(a)), print(len(b))



# append() - which of these works?
a = [1]
#a.append(2,3,4)
#a.append([2,3,4])






# TUPLE - I won't cover this, but there are some very neat things you do with them.
# this is a tuple:
(1, 2, 3)
firstname, lastname = ('Corvo', 'Attano')






# DICTIONARY
# these are dictionaries:
{}
# see purple?
dict()


# a dictionary is a collection of key:value pairs. Order doesn't matter. Trailing , is fine.
a = {'key2': 'value2', 'key1': 'value1', }
print(a)



# the key and value can be of mixed types:
a = {2:[], 1:'mercy', 'Coraline':5}
# to retrieve a value:
print(a[2])
# Python would complain
#print(a[3])
# to update an existing value (that key already exists):
a['April'] = 'Run Forrest'
print(a)
# to add a new key:value pair (the key doesn't yet exist):
a[7.62] = 'January'
print(a)
# to remove a k:v pair:
del a[1]
print(a)

# and of course, len() works
print(len(a))


# Keys are unique, but values don't have to be.
# If the key already exists, its value is updated. if not, it's added.
# Practise how to define, add, retrieve, update, and remove k:v pairs.
#
# ... or I kill this kitten.





# Further reading: look up the term "iterable"
# https://stackoverflow.com/a/9884501/4570438
#
# Advanced topic: List comprehension
# https://docs.python.org/3.6/tutorial/datastructures.html#list-comprehensions





# TEST:
# what the type of these?
9
'9'
['9']
('9')
{'9':9}

# which of them are True?
3 == '3'
3 > 2
#'3' > 2

d = {'g':'ghouls', 'h':'hags', 'w':'wraiths'}
d[7] = 'seven'
len(d)
d[7] + ' ' + d['w']
