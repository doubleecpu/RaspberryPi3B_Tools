#!/usr/bin/env python3
# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/   

from  tkinter import * 
from SetupFiles.Views import Linux_View as Views

root = Tk() #tkinter Window

class Window_Manager:
    def __init__(self, parent):
        global root
        #reference main App 
        self.MVC_App = parent.MVC_App
        self.App_Name = "Window_Manager"
        #setup main window for Sensors App
        self.main_window = root
        self.LARGE_FONT= ("Verdana", 12)
        self.main_window.title = "Sensors App"
        self.frame = Frame(self.main_window)
        #sets up the first window to appear
        self.app_window = Views.get_win(self, self, Views.Win1)
        # display Menu 
        self.main_window.config(menu = self.menubar)

    def create_button(self, _class, **kwLayout):
        "Button that creates a new window"
        print(kwLayout['caption'], kwLayout['row'], kwLayout['column'])
        Button(self.main_window, text=kwLayout['caption'], command=lambda: self.new_window(_class)).grid( row=kwLayout['row'], column=kwLayout['column'])
  
    def show_widgets(self):
        self.create_button(Views.Win1, caption="Click to open Main Window", row = 1, column = 1)
        self.create_button(Views.Win2, caption='Click to open OS Check', row = 1, column = 2) 
        self.create_button(Views.Win3, caption='Click to open SW Check', row = 1, column = 3)   
        self.create_menubars()

    def new_window(self, _class):
        Views.get_win(self, self, Views.Win1)
        self.frame = _class(self).frame
        
    def create_menubars(self):
        # Creating Menubar 
        self.menubar = Menu(self.main_window )
        # Adding File Menu and commands 
        self.file = Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='File', menu = self.file) 
        self.file.add_command(label ='New File', command = None) 
        self.file.add_command(label ='Open...', command = None) 
        self.file.add_command(label ='Save', command = None) 
        self.file.add_separator() 
        self.file.add_command(label ='Exit', command = root.destroy) 

        self.edit = Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='Edit', menu = self.edit) 
        self.edit.add_command(label ='Cut', command = None) 
        self.edit.add_command(label ='Copy', command = None) 
        self.edit.add_command(label ='Paste', command = None) 
        self.edit.add_command(label ='Select All', command = None) 
        self.edit.add_separator() 
        self.edit.add_command(label ='Find...', command = None) 
        self.edit.add_command(label ='Find again', command = None) 
  
        # Adding Help Menu 
        self.help_ = Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='Help', menu = self.help_) 
        self.help_.add_command(label ='Tk Help', command = None) 
        self.help_.add_command(label ='Demo', command = None) 
        self.help_.add_separator() 
        self.help_.add_command(label ='About Tk', command = None) 
         
    def mainloop(self):
        #The Sensors App Window Appear
        self.main_window.mainloop()