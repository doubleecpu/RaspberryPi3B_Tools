#!/usr/bin/env python3
# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/   

import tkinter as i_tk
#from tkinter.ttk import * 
from time import strftime
app_main_Window = i_tk.Tk #tkinter Window
app_main_Menubar = i_tk.Menu #tkinter menubar
app_sub_Frame = i_tk.Frame  #tkinter Frame
Lbl = i_tk.Label #tkinter Label
Btn = i_tk.Button #tkinter Button

LARGE_FONT= ("Verdana", 12)
class PageView(app_main_Window):
    def __init__(self, *args, **kwargs):
        app_main_Window.__init__(self, *args, **kwargs)
        self.hsize = 480
        self.vsize = 240
        app_main_Window.geometry(self, str(self.hsize) + "x" + str(self.vsize))
        app_main_Window.title(self, 'Sensors App')
        # Creating Empty Menubar 
        self.menubar = app_main_Menubar(self)
        
        self.add_File_To_Menubar()
        # self.view_add_status()
        self.add_Help_To_Menubar()
        # display Menu 
        app_main_Window.config(self, menu = self.menubar, bg="white")
        self.container = app_sub_Frame(self, bg="red", bd="10")
        self.container.grid_rowconfigure(4, weight=10)
        self.container.grid_columnconfigure(2, weight=10)
        self.container.pack( side="top", fill="both", expand = False)
        self.frames = {}
        for F in (StartPage, ViewPageOne, ViewPageTwo, ViewAboutPage):
            app_main_Window.frame = F(self.container, self)
            self.frames[F] = app_main_Window.frame
            app_main_Window.frame.grid(row=1, column=1, sticky="W")
 
        self.show_frame(StartPage)

    def add_File_To_Menubar(self):
        # Adding File Menu and commands 
        self.file = app_main_Menubar(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='File', menu = self.file) 
        self.file.add_command(label ='SW Status', command = None) 
        self.file.add_command(label ='Print Status...', command = None) 
        self.file.add_command(label ='Save Text', command = None) 
        self.file.add_separator() 
        self.file.add_command( label ='Quit', command = None) 

    def add_Help_To_Menubar(self):
        # Adding Help Menu 
        self.help_ = app_main_Menubar(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='Help', menu = self.help_) 
        self.help_.add_command(label ='Online Help', command = None) 
        self.help_.add_command(label ='Demo', command = None) 
        self.help_.add_separator() 
        self.help_.add_command(label ='About Sensors',  command=lambda: self.show_frame(ViewAboutPage))

    def show_frame(self, cont):
        self.frame = self.frames[cont]
        self.frame.tkraise()

    def view_loop(self):
        i_tk.mainloop()
        
class StartPage(app_sub_Frame):
    def __init__(self, parent, controller):
        app_sub_Frame.__init__(self, parent, bg="blue")
        self.label = Lbl(self, text="Start Page", font=LARGE_FONT, bg="white")
        self.label.pack(pady=10,padx=10)
        # Add Buttons
        self.button = Btn(self, text="Visit Page 1", command=lambda: controller.show_frame(ViewPageOne), bg="white")
        self.button.pack()
        self.button2 = Btn(self, text="Visit Page 2", command=lambda: controller.show_frame(ViewPageTwo), bg="white")
        self.button2.pack()
        self.button3 = Btn(self, text="New Button", command=lambda: controller.show_frame(ViewPageOne), bg="white")
        self.button3.pack()

class ViewPageOne(i_tk.Frame):

    def __init__(self, parent, controller):
        app_sub_Frame.__init__(self, parent, bg="green")
        self.label = Lbl(self, text="Page One!!!", font=LARGE_FONT, bg="green")
        self.label.pack(pady=10,padx=10)
        self.button1 = Btn(self, text="Back to Home", command=lambda: controller.show_frame(StartPage), bg="white")
        self.button1.pack()
        self.button2 = Btn(self, text="Page Two", command=lambda: controller.show_frame(ViewPageTwo), bg="white")
        self.button2.pack()

class ViewPageTwo(app_sub_Frame):
    def __init__(self, parent, controller):
        app_sub_Frame.__init__(self, parent, bg="cyan")
        self.label = Lbl(self, text="Page Two!!!", font=LARGE_FONT, bg="white")
        self.label.pack(pady=10,padx=10)
        self.button1 = Btn(self, text="Back to Home", command=lambda: controller.show_frame(StartPage), bg="white")
        self.button1.pack()
        self.button2 = Btn(self, text="Page One", command=lambda: controller.show_frame(ViewPageOne), bg="white")
        self.button2.pack()

class ViewAboutPage(app_sub_Frame):
    def __init__(self, parent, controller):
        app_sub_Frame.__init__(self, parent, bg="fuchsia")
        self.label = Lbl(self, text="About Page", font=LARGE_FONT, bg="white")
        self.label.pack(pady=10,padx=10)
        self.button1 = Btn(self, text="Back to Home", command=lambda: controller.show_frame(StartPage), bg="white")
        self.button1.pack()
