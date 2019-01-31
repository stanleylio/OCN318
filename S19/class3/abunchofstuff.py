'''This is a script that generates a random
number and tells you if your guess is correct.

https://xkcd.com/221
'''
# 01/28/2019
import random, math

random.seed()

rand_number = random.random()
#print(rand_number, type(rand_number))

sol = rand_number*100
#print(sol, type(sol))

# int() truncates towards 0
# compare this to round()
sol = int(sol)
#print(sol, type(sol))

# - - - fancy separator - - -

# Case matters; indentation matters;
# Use the Tab key for indentation
# Don't mix editor or indentation markers
# Your, you're; their, there...
count = 0
while True:
    count += 1
    guess = int(input('Enter your guess:'))
    if guess > sol:
        print('Your guess {} is too high'.format(guess))
    elif guess < sol:
        print('Your guess {} is too low'.format(guess))
    else:
        break



print('Took you {} tries'.format(count))

if count > math.log(100, 2):
    print('lame')
elif count > math.log(100, 2)/2:
    print('tolerable')
else:
    print('what are the odds')
