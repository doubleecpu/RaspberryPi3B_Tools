#!/usr/bin/python3

# Controls how Data is to be displayed on the app

from Model import Model_OSRelease
from Setup_Scripts.LAMP_Server import LAMP_Database
from Setup_Scripts.Wordpress import Wordpress_Host
from View import Window_Manager
import sys as App_sys
import subprocess as Sub_Process

class IControl_View:
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
        self.Bash_Script = IRun_Bash(self)
        self.Bash_Script.Create_LAMP_Server()
    
    def Run_WP_Setup(self):
        self.WP_Script = IRun_Bash(self)
        self.WP_Script.Create_WP_Host()

class IRun_Bash:
    def __init__(self, Control_Viewer):
        self.Controller = Control_Viewer.MVC_App.Controller
        self.subprocess = Sub_Process
        self.LAMP_DB = LAMP_Database.Bash_DB
        self.WP_Host = Wordpress_Host.WP_Host

    def Create_LAMP_Server(self):
        self.DB_Stack = 'LAMP'
        self.LAMP_DB.Create_DB(self, self)
    
    def Create_WP_Host(self):
        self.Host = 'Wordpress'
        self.WP_Host.Create_Host(self, self)