#!/usr/bin/python

from Sensor_Factory import Sensor_Factory
from Sensor_Database import Sensor_Database

def Use_Ultrasonic():
    Sensor1 = Sensor_Factory.Sensors('HCSR04', [23, 24, .1])
    Sensor1.readConsole()
    
def Check_Database():
    if Sensor_Database.hasPHP():
        Use_Kit()
    elif read('i:install') == 'i':
        print('installing')
    else:
        print('no database')
        
def Use_Temperature_Humidity():
    Sensor2 = Sensor_Factory.Sensors('DHT11',4)
    Sensor2.readConsole()
        
    
Use_Temperature_Humidity()
