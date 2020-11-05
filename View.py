#!/usr/bin/env python3  

from SetupFiles.Views import Linux_View as Views


class Window_Manager:
    def __init__(self, parent):
        #reference main App 
        self.MVC_App = parent.MVC_App
        self.App_Name = "Window_Manager"
        #setup main window for Sensors App
        self.LARGE_FONT= ("Verdana", 10)
        #sets up the first window to appear
        self.app_window = Views.get_win(self, Views.Win1)
        
        # display Menu 
        self.app_window.title = "Sensors App"
        #self.app_window..config(menu = self.menubar)
        
    def mainloop(self):
        #The Sensors App Window Appear
        self.app_window.tk.mainloop()