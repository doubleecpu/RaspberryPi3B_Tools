#!/usr/bin/python3

# Controls how Data is to be displayed on the app

from Model import Model_OSRelease
from Sensor_Database.LAMP_Server import LAMP_Database
from View import Window_Manager
import sys as App_sys
import subprocess as Sub_Process

class Control_View:
    def __init__(self, parent):
        self.MVC_App = parent.app
        self.App_sys = App_sys
        self.App_Name = "Control_View"
        parent.controller = self
        # creates OS Data Using Functions  
        self.OS_Model = Model_OSRelease(self)
        #self.OS_Model.Test_OS()

        # Creates Windows To Hold OS Data
        self.app = Window_Manager(self)
    
    def Control_View_Loop(self):
        self.app.view_loop()

    def Run_Bash(self):
        self.Bash_Script = Control_Bash(self)
        self.Bash_Script.Create_LAMP_Server()

class Control_Bash:
    def __init__(self, Control_Viewer):
        self.Controller = Control_Viewer.MVC_App.Controller
        self.subprocess = Sub_Process
        self.LAMP_DB = LAMP_Database.Bash_DB

    def Create_LAMP_Server(self):
        self.DB_Stack = 'LAMP'
        self.LAMP_DB.Create_DB(self, self)