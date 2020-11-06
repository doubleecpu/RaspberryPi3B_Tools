#!/usr/bin/env python3

import Controller

class MVC_App:
    def __init__(self):
        self.app = self 
        self.version = "0.0.2"
        self.Setup_Page = None
        self.App_Name = "MVC_APP (RaspberryPi 3 Sensors)"
        print("Starting Sensors MVC App")
        

    def application_loop(self):
        Controller.Control_View(self)
        #self.Sensors_App_View.Fill_Data(self.Sensors_App_View)
        #self.Sensors_App_View.view_loop()

MyApp = MVC_App()
MyApp.application_loop()