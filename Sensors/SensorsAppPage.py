# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/   

import tkinter as tk
from tkinter.ttk import * 
from time import strftime

LARGE_FONT= ("Verdana", 12)

class PageView(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.title('Sensors App') 
        # Creating Menubar 
        self.menubar = tk.Menu(self) 
        self.view_add_file()
        # self.view_add_status()
        self.view_add_help()
        # display Menu 
        tk.Tk.config(self, menu = self.menubar)
        self.container = tk.Frame(self, bg="white")
        self.container.pack(side="top", fill="both", expand = True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            tk.Tk.frame = F(self.container, self)
            self.frames[F] = tk.Tk.frame
            tk.Tk.frame.grid(row=0, column=0, sticky="nsew")
 
        self.show_frame(StartPage)

    def show_frame(self, cont):
        self.frame = self.frames[cont]
        self.frame.tkraise()

    def view_add_file(self):
        # Adding File Menu and commands 
        self.file = tk.Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='File', menu = self.file) 
        self.file.add_command(label ='SW Status', command = None) 
        self.file.add_command(label ='Print Status...', command = None) 
        self.file.add_command(label ='Save Text', command = None) 
        self.file.add_separator() 
        self.file.add_command(label ='Quit', command = tk.Tk.destroy) 

    def view_add_help(self):
        # Adding Help Menu 
        self.help_ = tk.Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='Help', menu = self.help_) 
        self.help_.add_command(label ='Online Help', command = None) 
        self.help_.add_command(label ='Demo', command = None) 
        self.help_.add_separator() 
        self.help_.add_command(label ='About Sensors', command = None) 

    def view_loop(self):
        tk.mainloop()
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        self.label.pack(pady=10,padx=10)
        self.button = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        self.button.pack()
        self.button2 = tk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        self.button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        self.label.pack(pady=10,padx=10)
        self.button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        self.button1.pack()
        self.button2 = tk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        self.button2.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        self.label.pack(pady=10,padx=10)
        self.button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        self.button1.pack()
        self.button2 = tk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        self.button2.pack()
        



