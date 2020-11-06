#!/usr/bin/env python3
import tkinter as tkint  

# Parent View
class View_1:
    def __init__(self, win_manager, Class_Name):
        self.win_manager = win_manager
        self.App_Name = Class_Name 
        self.MVC_App = win_manager.MVC_App
        self.tk = tkint
        self.row_count = 1 
        self.column_count = 1

    def increment_row(self):
        self.row_count = self.row_count + 1
        return self.row_count

    def Software_Info(self, Caption, Lbl_BG, Data, Txt_BG):
        create_Label_Text(self, caption=Caption, font=self.win_manager.LARGE_FONT, bg=Lbl_BG, row=self.increment_row(), column=self.column_count)
        create_Label_Text(self, caption=Data, font=self.win_manager.LARGE_FONT, bg=Txt_BG, row=self.increment_row(), column=self.column_count)
    
    def create_Label_Text(self, _win, **kwLayout):
        #Adds Button that creates a new window
        _win.tk.Label(_win.app_window, text=kwLayout['caption'], font=kwLayout['font'], bg=kwLayout['bg']).grid( row=kwLayout['row'], column=kwLayout['column'])

    def show_default_widgets(self._win):
        self.create_button(_win, Win1, caption="Click to open Main Window", App_Name="Main Window", row = 1, column = 1)
        self.create_button(_win, Win2, caption='Click to open OS Check', App_Name="OS Check", row = 1, column = 2) 
        self.create_button(_win, Win3, caption='Click to open SW Check', App_Name="SW Check", row = 1, column = 3)  

    def create_button(self, _win, _view, **kwLayout):
        "Adds Button that navigates to next window"
        _win.tk.Button(_win.app_window, text=kwLayout['caption'], command=lambda: next_view(_win, kwLayout['App_Name'], _view)).grid( row=kwLayout['row'], column=kwLayout['column'])


class Win1(View_1):
    def __init__(self, win_manager):
        View_1.__init__(self, win_manager, "Main Window")   
        self.app_window = win_manager.check_views(self.App_Name)
        #Checks if App_window is set to string or View
        if self.app_window == "View Not Found":
            new_window(self)
            self.win_manager.add_views(self)
            self.frame = self.tk.Frame(self.app_window, bg="white").grid(row=3, column=3)
            create_default_menubars(self)
            show_default_widgets(self)

class Win2(View_1):
    def __init__(self, win_manager):
        View_1.__init__(self, win_manager, "OS Check")
        self.app_window = win_manager.check_views(self.App_Name)
        #Checks if App_window is set to string or View
        if self.app_window == "View Not Found":
            new_window(self)
            self.win_manager.add_views(self)
            self.OS_Info = win_manager.MVC_App.controller.OS_Model.OS_Info
            create_default_menubars(self)
            show_default_widgets(self)
            self.show_widgets()

    def show_widgets(self):
        "List of Data gathered about OS"
        self.tk.Frame(self.app_window, bg="white").grid(row=3, column=3)
     
        self.Software_Info("PRETTY NAME",'light grey', self.OS_Info.PRETTY_NAME, 'white')
        self.Software_Info("NAME",'light grey', self.OS_Info.NAME, 'white')
        self.Software_Info("VERSION_ID",'light grey', self.OS_Info.VERSION_ID, 'white')
        self.Software_Info("VERSION",'light grey', self.OS_Info.VERSION, 'white')
        self.Software_Info("VERSION_CODENAME",'light grey', self.OS_Info.VERSION_CODENAME, 'white')
        self.Software_Info("ID",'light grey', self.OS_Info.ID, 'white')
        self.Software_Info("ID_LIKE",'light grey', self.OS_Info.ID_LIKE, 'white')
        self.Software_Info("HOME_URL",'light grey', self.OS_Info.HOME_URL, 'white')

class Win3(View_1):
    def __init__(self, win_manager):
        View_1.__init__(self, win_manager, "SW Check")
        self.app_window = win_manager.check_views(self.App_Name)
        #Checks if App_window is set to string or existing View
        if self.app_window == "View Not Found":
            new_window(self)
            self.win_manager.add_views(self)
            self.SW_Info = win_manager.MVC_App.controller.OS_Model.SW_Info
            self.frame = self.tk.Frame(self.app_window, bg="white").grid(row=3, column=3)
            self.menubar = self.tk.Menu(self.app_window)
            #Setup Window
            create_default_menubars(self)
            show_default_widgets(self)
            self.show_widgets()

    def show_widgets(self):
        #Add THe SW Check Results
        self.Software_Info("Python3 Version",'light grey', self.SW_Info.Python3_Version, 'white')
        self.Software_Info("GPIO",'light grey', self.SW_Info.GPIO_Version, 'white')
        self.Software_Info("I2C",'light grey', self.SW_Info.I2C_Version, 'white')
        self.Software_Info("SPI",'light grey', self.SW_Info.SPI_Version, 'white')
        self.Software_Info("UART",'light grey', self.SW_Info.UART_Version, 'white')
        self.Software_Info("MySQL",'light grey', self.SW_Info.MySQL_Version, 'white')
        self.Software_Info("Apache",'light grey', self.SW_Info.Apache_Version, 'white')
        self.Software_Info("PHP",'light grey', self.SW_Info.PHP_Version, 'white')

def create_default_menubars(_win):
    # Creating Menubar 
    _win.menubar = _win.tk.Menu(_win.app_window)
    # Adding File Menu and commands  
    _win.file = _win.tk.Menu(_win.menubar, tearoff = 0) 
    _win.menubar.add_cascade(label ='File', menu = _win.file) 
    _win.file.add_command(label ='New File', command = None) 
    _win.file.add_command(label ='Open...', command = None) 
    _win.file.add_command(label ='Save', command = None) 
    _win.file.add_separator() 
    _win.file.add_command(label ='Exit', command=lambda: _win.tk.Tk.destroy(_win)) 

    _win.edit = _win.tk.Menu(_win.menubar, tearoff = 0) 
    _win.menubar.add_cascade(label ='Edit', menu = _win.edit) 
    _win.edit.add_command(label ='Cut', command = None) 
    _win.edit.add_command(label ='Copy', command = None) 
    _win.edit.add_command(label ='Paste', command = None) 
    _win.edit.add_command(label ='Select All', command = None) 
    _win.edit.add_separator() 
    _win.edit.add_command(label ='Find...', command = None) 
    _win.edit.add_command(label ='Find again', command = None) 
  
    # Adding Help Menu 
    _win.help_ = _win.tk.Menu(_win.menubar, tearoff = 0) 
    _win.menubar.add_cascade(label ='Help', menu = _win.help_) 
    _win.help_.add_command(label ='Tk Help', command = None) 
    _win.help_.add_command(label ='Demo', command = None) 
    _win.help_.add_separator() 
    _win.help_.add_command(label ='About Tk', command = None)
    #display on Window
    _win.app_window.config(menu = _win.menubar) 

# Window Manager Methods
def get_win(win_manager, _view):
    return _view(win_manager)

def initial_view(win_man, _view): 
    return _view(win_man)

# Common Window Methods
def new_window(_win):
    _win.app_window = _win.tk.Tk()
    _win.app_window.title(_win.App_Name)
    _win.win_manager.app_window = _win.app_window
   
def close_window(_win):
    _win.tk.Tk.destroy

def next_view(_win, _App_Name, _view):
    _check = _win.win_manager.check_views(_App_Name)
    #print(_win.App_Name)
    if _check == "View Not Found":       
        _win.win_manager.app_window = _view(_win.win_manager)
        _win.app_window = _win.win_manager.app_window
    else:
        _win.win_manager.app_window = _check
        _win.win_manager.app_window.app_window.focus
        
