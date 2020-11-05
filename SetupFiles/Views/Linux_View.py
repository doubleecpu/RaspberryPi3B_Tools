#!/usr/bin/env python3
import tkinter as tkint  

class Win1:
    def __init__(self, win_manager):
        self.win_manager = win_manager
        self.App_Name = "Main Window"
        self.MVC_App = win_manager.MVC_App
        self.tk = tkint 
        #self.app_window = self.tk.Tk()
        self.app_window = root
        self.app_window.title(self.App_Name)
        self.frame = self.tk.Frame(self.app_window, bg="white").grid(row=3, column=3)
        create_default_menubars(self)
        show_default_widgets(self)

class Win2:
    def __init__(self, win_manager):
        self.win_manager = win_manager
        self.App_Name = "OS Check"
        self.MVC_App = win_manager.MVC_App
        self.tk = tkint 
        self.app_window = self.tk.Tk()
        self.app_window.title(self.App_Name)
        self.app_window.focus
        self.OS_Info = win_manager.MVC_App.controller.OS_Model.OS_Info
        create_default_menubars(self)
        show_default_widgets(self)
        self.show_widgets()

    def show_widgets(self):
        self.row_count = 1 
        self.column_count = 0
        "List of Data gathered about OS"
        print(self.OS_Info.PRETTY_NAME)
        self.tk.Frame(self.app_window, bg="white").grid(row=3, column=3)
        create_Label_Text(self, caption="PRETTY NAME", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.PRETTY_NAME, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        #self.NAME = ""
        create_Label_Text(self, caption="NAME", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.NAME, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        
        #self.VERSION_ID = ""
        create_Label_Text(self, caption="VERSION_ID", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.VERSION_ID, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        #self.VERSION = ""
        create_Label_Text(self, caption="VERSION", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.VERSION, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        #self.VERSION_CODENAME = ""
        create_Label_Text(self, caption="VERSION_CODENAME", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.VERSION_CODENAME, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        #self.ID = ""
        create_Label_Text(self, caption="ID", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.ID, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        #self.ID_LIKE = ""
        create_Label_Text(self, caption="ID_LIKE", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.ID_LIKE, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        #self.HOME_URL = ""
        create_Label_Text(self, caption="HOME_URL", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.HOME_URL, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        #self.SUPPORT_URL = ""
        create_Label_Text(self, caption="SUPPORT_URL", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.SUPPORT_URL, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        #self.BUG_REPORT_URL = ""
        create_Label_Text(self, caption="BUG_REPORT_URL", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.BUG_REPORT_URL, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        
    def increment_row(self):
        self.row_count = self.row_count + 1
        return self.row_count

class Win3:
    def __init__(self, win_manager):
        self.win_manager = win_manager
        self.App_Name = "SW Check"
        self.MVC_App = win_manager.MVC_App
        #Open New Window
        self.tk = tkint 
        self.app_window = self.tk.Tk()
        self.app_window.title(self.App_Name)
        self.frame = self.tk.Frame(self.app_window, bg="white").grid(row=3, column=3)
        self.menubar = self.tk.Menu(self.app_window)
        #Setup Window
        create_default_menubars(self)
        show_default_widgets(self)
        self.show_widgets()

    def show_widgets(self):
        self.quit = self.tk.Button(self.frame, text=f"Quit this window n. 3", command=close_window(self))
        self.quit.grid(row=2, column=3)
        self.label = self.tk.Label(self.frame, text="THIS IS THIRD WINDOW")
        self.label.grid(row=1, column=1)

        #Add THe SW Check Results
        create_Label_Text(self, caption="NAME", font=self.win_manager.LARGE_FONT, bg='grey', row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=self.OS_Info.NAME, font=self.win_manager.LARGE_FONT, bg='white', row=self.increment_row(), column=self.column_count)
        

# Window Manager Methods
def get_win(win_manager, _class):
    return _class(win_manager)

def new_window(win_, _class):
    get_win(win_.app_window.win_manager, _class)
    win_.frame = _class(win_.app_window).frame

# Common Window Methods
def create_button(win_, _class, **kwLayout):
    "Adds Button that creates a new window"
    win_.tk.Button(win_.app_window, text=kwLayout['caption'], command=lambda: next_window(win_, _class)).grid( row=kwLayout['row'], column=kwLayout['column'])

def create_Label_Text(win_, **kwLayout):
    "Adds Button that creates a new window"
    win_.tk.Label(win_.app_window, text=kwLayout['caption'], font=kwLayout['font'], bg=kwLayout['bg']).grid( row=kwLayout['row'], column=kwLayout['column'])
      
def show_default_widgets(win_):
    create_button(win_, Win1, caption="Click to open Main Window", row = 1, column = 1)
    create_button(win_, Win2, caption='Click to open OS Check', row = 1, column = 2) 
    create_button(win_, Win3, caption='Click to open SW Check', row = 1, column = 3)  
    

def close_window(win_):
    win_.tk.Tk.destroy

def next_window(win_, _class):
    win_.win_manager.app_window = _class(win_.win_manager)
    win_.app_window = win_.win_manager.app_window


def create_default_menubars(win_):
    # Creating Menubar 
    win_.menubar = win_.tk.Menu(win_.app_window)
    # Adding File Menu and commands  
    win_.file = win_.tk.Menu(win_.menubar, tearoff = 0) 
    win_.menubar.add_cascade(label ='File', menu = win_.file) 
    win_.file.add_command(label ='New File', command = None) 
    win_.file.add_command(label ='Open...', command = None) 
    win_.file.add_command(label ='Save', command = None) 
    win_.file.add_separator() 
    win_.file.add_command(label ='Exit', command=lambda: win_.tk.Tk.destroy(win_)) 

    win_.edit = win_.tk.Menu(win_.menubar, tearoff = 0) 
    win_.menubar.add_cascade(label ='Edit', menu = win_.edit) 
    win_.edit.add_command(label ='Cut', command = None) 
    win_.edit.add_command(label ='Copy', command = None) 
    win_.edit.add_command(label ='Paste', command = None) 
    win_.edit.add_command(label ='Select All', command = None) 
    win_.edit.add_separator() 
    win_.edit.add_command(label ='Find...', command = None) 
    win_.edit.add_command(label ='Find again', command = None) 
  
    # Adding Help Menu 
    win_.help_ = win_.tk.Menu(win_.menubar, tearoff = 0) 
    win_.menubar.add_cascade(label ='Help', menu = win_.help_) 
    win_.help_.add_command(label ='Tk Help', command = None) 
    win_.help_.add_command(label ='Demo', command = None) 
    win_.help_.add_separator() 
    win_.help_.add_command(label ='About Tk', command = None)
    #display on Window
    win_.app_window.config(menu = win_.menubar) 