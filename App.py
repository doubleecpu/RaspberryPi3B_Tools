#!/usr/bin/python3

from Sensors import SensorsAppPage 

class app:
    def __init__(self):
        self.app = self 
        self.version = "0.0.1"
        self.Setup_Page = None
        self.App_Name = "RaspberryPi 3 Sensors" 
        self.Sensors_App_View = SensorsAppPage.PageView()

    def application_loop(self):
        print("Starting GUI")
        self.Sensors_App_View.view_loop()
        
MyApp = app()
MyApp.application_loop()



