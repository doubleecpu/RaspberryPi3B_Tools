#!/usr/bin/python

import array as Pins
from Sensor_Factory.HCSR04.Ultrasonic import Sensor as Create_HCSR04
from Sensor_Factory.DHT11.Temperature_Humidity import Sensor as Create_DHT11

def Sensors(Object_Type, Pins):
    if Object_Type == "HCSR04":
        Sensor_object = Create_HCSR04(Pins[0], Pins[1], Pins[2]).getSensor()
    
    elif Object_Type == "DHT11":
        Sensor_object = Create_DHT11(Pins).getSensor()

    return Sensor_object    
#To Test Remove: from Sensor_Factory.
#Sensors("HCSR04", [23, 24, 0.1])