import time
import RPi.GPIO as GPIO

whatever = 17

# boilerplate
GPIO.setmode(GPIO.BCM)
GPIO.setup(whatever, GPIO.OUT)

# repeat this forever:
while True:
    # turn ON
    GPIO.output(whatever, GPIO.HIGH)
    # wait
    time.sleep(0.001)
    # turn OFF
    GPIO.output(whatever, GPIO.LOW)
    # wait again
    time.sleep(0.009)
