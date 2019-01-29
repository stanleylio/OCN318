import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

k = 0.1

while True:
    try:
        for i in range(3):
            GPIO.output(5,GPIO.HIGH)
            time.sleep(k)
            GPIO.output(5,GPIO.LOW)
            time.sleep(k)

        for i in range(3):
            GPIO.output(6,GPIO.HIGH)
            time.sleep(k)
            GPIO.output(6,GPIO.LOW)
            time.sleep(k)
    except KeyboardInterrupt:
        print('user interrupted')
        break

GPIO.cleanup(5)
GPIO.cleanup(6)
