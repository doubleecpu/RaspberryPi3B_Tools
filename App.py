#!/usr/bin/python3

import Controller

class MVC_App:
    def __init__(self):
        self.app = self 
        self.version = "0.0.2"
        self.Setup_Page = None
        self.App_Name = "MVC_APP (RaspberryPi 3 Sensors)"
        print("Starting Sensors MVC App")
        self.Controller = Controller.Control_View(self)

    def application_loop(self):
        self.Controller.Control_View_Loop()

    def App_Close(self):
        sys

MyApp = MVC_App()
MyApp.application_loop()