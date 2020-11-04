#!/usr/bin/env python3

from Sensors import SensorsAppPage 
import Controller #, Model, View

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

class MVC_App:
    def __init__(self):
        self.app = self 
        self.version = "0.0.2"
        self.Setup_Page = None
        self.App_Name = "MVC_APP (RaspberryPi 3 Sensors)"
        print("Starting GUI")
        

    def application_loop(self):
        Controller.Control_View(self)
        #self.Sensors_App_View.Fill_Data(self.Sensors_App_View)
        #self.Sensors_App_View.view_loop()

MyApp = MVC_App()
MyApp.application_loop()