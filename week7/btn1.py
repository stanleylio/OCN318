# GPIO - input
# print something when button is pressed
#   keep printing as long as button is held down
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.LOW == GPIO.input(18):
        print('ding!')
    time.sleep(0.1)
