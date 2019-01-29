# Class
# "The best material model of a cat is another, or preferably the same, cat."
#
# You probably won't define your own in this class, but you will have to know how to use someone else's.
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18




# this defines a CLASS (indentation matters! a lot!):
class Mordor:
    pass




# create an INSTANCE of a class and point a variable to it so you can refer to it later
m = Mordor()





# a class can contain stuff like literals and functions
class Mordor:
    locations = ['front yard', 'dungeon', 'driveway', 'bathroom']

    # now any instances of type Mordor would have a method called "walk_int()"
    def walk_into(self, v):
        return 'one does not simply ' + v

# and you use them like this:
m = Mordor()
for loc in m.locations:
    print(loc)

print(m.walk_into('open the pod bay door'))
print(type(m.walk_into("it doesn't have to make sense")))   # if a function returns a string...
print(m.walk_into('shows up') + ' during office hours')     # you treat it like a string (slice, split, concatenation, format...)


# This won't make any sense to you (it made no sense to me when I was in college) until
# you actually use it. For now it's enough to know how to recognize a class definition
# and how you can use it. The "why" and "when" will come natually in problem solving.
