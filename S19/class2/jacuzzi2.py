import time
import RPi.GPIO as GPIO

whatever = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(whatever, GPIO.OUT)

P = 0.001

while True:
    
    for i in range(0, 1000, 1):
        r = i/1000
        GPIO.output(whatever, GPIO.HIGH)
        time.sleep(r*P)
        GPIO.output(whatever, GPIO.LOW)
        time.sleep((1-r)*P)
        
    for i in range(1000, 0, -1):
        r = i/1000
        GPIO.output(whatever, GPIO.HIGH)
        time.sleep(r*P)
        GPIO.output(whatever, GPIO.LOW)
        time.sleep((1-r)*P)
