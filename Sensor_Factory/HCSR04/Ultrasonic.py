#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class Sensor:
    def __init__(self, Trigger_Pin, Echo_Pin, Sleep_Time):
        self.name = 'HCSR04'
        self.Trigger = Trigger_Pin
        self.Echo = Echo_Pin
        self.Sleep = Sleep_Time
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Trigger,GPIO.OUT)
        print("Set up Trigger on Pin: ", self.Trigger)
        GPIO.setup(self.Echo,GPIO.IN)
        print("Set up Echo on Pin: ", self.Echo)
        GPIO.output(self.Trigger, False)
        print("Waiting For Sensor To Settle")
        time.sleep(1)
        print("Distance Measurement In Progress")
        return 
 
    def __del__(self):
        GPIO.cleanup()
    
    def getSensor(self):
        return self
        
    def readConsole(self):
        print("Entering Read Loop")
        pulse_start = 0
        while True:
            GPIO.output(self.Trigger, True)
            time.sleep(self.Sleep)
            GPIO.output(self.Trigger, False)
            
            while GPIO.input(self.Echo)==0:
                pulse_start = time.time()
                                
            while GPIO.input(self.Echo)==1:
                pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start
                distance = pulse_duration * 17150
                distance = round(distance, 2)

            print("Distance",distance,"cm")


