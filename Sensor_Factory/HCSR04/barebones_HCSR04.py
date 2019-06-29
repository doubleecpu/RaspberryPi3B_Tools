#!/usr/bin/python

import RPi.GPIO as GPIO
import time

Trigger = 23
Echo = 24
Sleep = .1
print("Initialized Pin Settings")
GPIO.setmode(GPIO.BCM)
print("Distance Measurement In Progress")
GPIO.setup(Trigger,GPIO.OUT)
print("Set up Pin: %d As Trigger", Trigger)
GPIO.setup(Echo,GPIO.IN)
print("Set up Pin: %d As Echo", Echo)
GPIO.output(Trigger, False)
print("Waiting For Sensor To Settle")
time.sleep(1)
print("Entering Read Loop")

while (True):
    GPIO.output(Trigger, True)
    time.sleep(Sleep)
    GPIO.output(Trigger, False)

    while GPIO.input(Echo)==0:
        pulse_start = time.time()

    while GPIO.input(Echo)==1:
        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

    print("Distance",distance,"cm")

GPIO.cleanup()
