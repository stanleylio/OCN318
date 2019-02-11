# Organization: function and module
# "Aircraft carriers are modular. If a toilet gets clogged, it doesn't start launching nuclear missiles."
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18, S19


# this defines a function called "haha":
def haha():
    pass
# you call it like this:
haha()
# (it does nothing)

# to see what it returns:
print(haha())
# so it does nothing, and returns nothing






def purpose():
    return "You pass butter"
# this still does nothing
purpose()
# but it returns something
print(purpose())
# Since it returns a string, you use it like a string:
print(type(purpose()))
print(purpose().split(' '))
print(purpose().replace('You', 'Thou shalt not'))





# this function accepts one ARGUMENT:
def add_one(v):
    return v + 1
print(add_one(3))





# this defines a function called "hunt" that expects one argument called "v".
def hunt(v):
    if 1 == v:
        return 'brave and bold'
    elif 2 == v:
        return 'heartless cold'
    elif 3 == v:
        return 'paid in coin of gold'
    else:
        return "it's beyond my paygrade"

for i in range(5):
    print(hunt(i))

# (optional) the ARGUMENT "v" is only defined within the function. So this is invalid:
#print(v)






# more examples:
def c2f(c):
    """Celsius to Fahrenheit"""
    return 9/5*c + 32

def f2c(f):
    """Fahrenheit to Celsius"""
    return (f - 32)*5/9

C = 25
print('{} Deg.C = {} Deg.F'.format(C, c2f(C)))
print(f2c(c2f(f2c(c2f(f2c(c2f(25)))))))     # why would you do this? but you could.


# Exercise: complete these two
def mg_L_to_uM(mgl):
    """convert a mg/L reading to uM"""
    pass

def uM_to_mg_L(uM):
    """convert a uM reading to mg/L"""
    pass

print('{} mg/L O2 = {} uM'.format(4, mg_L_to_uM(4)))
print('{} uM O2 = {} mg/L'.format(222, uM_to_mg_L(222)))





# - - - - -
# (optional)
# you get a copy of the variable, not the original
def mo(v):
    v = v + 3
    return v

v = 3
# calling mo() doesn't affect v - it's not the same v
mo(v)
print(v)

def mo(v):
    v.append(43)
    return v

li = []
print(li)
# - - - - -




# standard library - the datetime module
from datetime import datetime, timedelta


print('Time is now (HST): {}'.format(datetime.now()))
print('Time is now (UTC): {}'.format(datetime.utcnow()))

span = datetime(1945, 9, 2) - datetime(1939, 9, 1)
print(type(span))
print('The fighting lasted {} years'.format(span.days/365))
print('The fighting lasted {} seconds'.format(span.total_seconds()))

# https://www.google.com/search?client=firefox-b-1&q=american+life+expectancy
expirationdate = datetime(1990, 1, 1) + timedelta(days=365.25*78.69)
print(type(expirationdate))
print(expirationdate)



# standard library - the time module
import time
print(time.time())
time.sleep(1)
print(time.time())






# See also: UNIX time: https://en.wikipedia.org/wiki/Unix_time
#
# A tour of the git repo "node"
