#!/usr/bin/env python3

import importlib.util  
import sys
import subprocess as cli_prompt 

class SW_Installed:
    def __init__(self):
        print("- Gathering Software Modules Installed")
        self.Python3_Version = ""
        self.GPIO_Version = []
        self.I2C_Version = []
        self.SPI_Version = []
        self.UART_Version = []
        self.MySQL_Version = []
        self.Apache_Version = []
        self.PHP_Version = ''
        self.check_Python()
        self.check_Comms()
        self.check_LAMP()

    def Print_Values(self):
        print("-- Python version is: 3." +  self.Python3_Version) 
        print("-- Checking Python Modules")
        print("--- GPIO  : ", *self.GPIO_Version)
        print("--- I2C   : ", *self.I2C_Version)
        print("--- SPI   : ", *self.SPI_Version)
        print("--- UART  : ", *self.UART_Version)

        print("-- Checking LAMP Stack")
        print("--- MySQL : ", *self.MySQL_Version)
        print("--- Apache: ", *self.Apache_Version)
        print("--- " + self.PHP_Version) 
        
        print("Checking NodeJS")

        print("Checking Wordpress")

        print("Finished Checking Software")


    def check_Python(self):
        try: 
            self.Python3_Version =  str(sys.version_info.minor)
        except: 
            self.Python3_Version = "Not Founnd using sys."
    
    def check_Comms(self): 
        self.GPIO_Version.append([self.is_Available('RPi')])
        self.GPIO_Version.append([self.is_Available('pigpio')])
        self.GPIO_Version.append([self.is_Available('gpiozero')])

        self.I2C_Version.append([self.is_Available('smbus')])
        self.SPI_Version.append([self.is_Available('spidev')])
        self.UART_Version.append([self.is_Available('serial')])
        self.UART_Version.append([self.is_Available('io')])
        

    def is_Available(self, Property_Name): 
        try :
            Ver_ = importlib.find_loader(Property_Name)
            if Ver_ is not None:
                Property_Name = Property_Name + " Available"
            else:
                Property_Name = Property_Name + " N/A"
            return Property_Name
        except : 
            return Property_Name + " Exception Occurred"
    
    def check_LAMP(self):
        self.MySQL_Version.append([self.is_Available('MySQLdb')])
        self.MySQL_Version.append([self.is_Available('mysql-connector-python')])
        self.MySQL_Version.append([self.is_Available('SQLite')])
        self.Apache_Version.append([self.is_Available('mod_wsgi')])
        self.check_PHP()
    
    def check_PHP(self):
        try:
            self.PHP_Version = cli_prompt.run(['php', '-v'], capture_output=True)
            self.PHP_Version = str(self.PHP_Version.stdout[0:9])[2:9]
        except:
            self.PHP_Version = "PHP N/A"
