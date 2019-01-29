# GPIO - input
# use the push button as a "toggle switch"
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

tv_is_on = False

while True:
    
    while GPIO.HIGH == GPIO.input(18):
        time.sleep(0.001)

    tv_is_on = not tv_is_on
    
    if tv_is_on:
        print('TV is ON')
    else:
        print('TV is OFF')
    
    while GPIO.LOW == GPIO.input(18):
        time.sleep(0.001)

# Homework idea: use the button to toggle an LED ON and OFF: press it once to turn ON, press it again to turn OFF
# Challenge: have two LEDs called A and B, one is ON and the other is OFF. Push the button once and they reverse
# their states (ON becomes OFF and vice versa).
