# GPIO - input
# print something when button is pressed
#   print once and only once per button press
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    
    while GPIO.HIGH == GPIO.input(18):
        time.sleep(0.001)

    print('ding!')
    
    while GPIO.LOW == GPIO.input(18):
        time.sleep(0.001)

# Something to think about: this only works for one button (why?). What if I have
# more than one button? Say I have to buttons. One button prints "A", the other, "B".
# (a good final exam question)
