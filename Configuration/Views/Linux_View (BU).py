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
        self.create_Label_Text( caption=Caption, font=self.win_manager.LARGE_FONT, bg=Lbl_BG, row=self.increment_row(), column=self.column_count)
        self.create_Label_Text( caption=Data, font=self.win_manager.LARGE_FONT, bg=Txt_BG, row=self.increment_row(), column=self.column_count)
    
    def create_Label_Text(self, **kwLayout):
        #Adds Button that creates a new window
        self.tk.Label(self.app_window, text=kwLayout['caption'], 
                      font=kwLayout['font'], bg=kwLayout['bg']
                      ).grid( 
                          sticky='WE', 
                          row=kwLayout['row'], 
                          column=kwLayout['column']
                          )

    def create_button(self, _view, **kwLayout):
        "Adds Button that navigates to next window"
        self.tk.Button(self.app_window, 
                     text=kwLayout['caption'],
                     command=lambda: next_view(self, kwLayout['App_Name'], _view)
                     ).grid( 
                         sticky='WE', 
                         row=kwLayout['row'], 
                         column=kwLayout['column']
                         )

    def show_default_widgets(self):
        self.create_button( Win1, caption="Click to open Main Window", App_Name="Main Window", row = 1, column = 1)
        self.create_button( Win2, caption='Click to open OS Check', App_Name="OS Check", row = 1, column = 2) 
        self.create_button( Win3, caption='Click to open SW Check', App_Name="SW Check", row = 1, column = 3)  

    def close_window(self):
        self.win_manager.remove_view(self)
        self.tk.Tk.destroy(self.app_window)

    def create_default_menubars(self):
        # Creating Menubar 
        self.menubar = self.tk.Menu(self.app_window)
        # Adding File Menu and commands  
        self.file = self.tk.Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='File', menu = self.file) 
        self.file.add_command(label ='New File', command = None) 
        self.file.add_command(label ='Open...', command = None) 
        self.file.add_command(label ='Save', command = None) 
        self.file.add_separator() 
        self.file.add_command(label ='Exit', command=lambda: self.close_window()) 

        self.edit = self.tk.Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='Edit', menu = self.edit) 
        self.edit.add_command(label ='Cut', command = None) 
        self.edit.add_command(label ='Copy', command = None) 
        self.edit.add_command(label ='Paste', command = None) 
        self.edit.add_command(label ='Select All', command = None) 
        self.edit.add_separator() 
        self.edit.add_command(label ='Find...', command = None) 
        self.edit.add_command(label ='Find again', command = None) 
  
        # Adding Help Menu 
        self.help_ = self.tk.Menu(self.menubar, tearoff = 0) 
        self.menubar.add_cascade(label ='Help', menu = self.help_) 
        self.help_.add_command(label ='Tk Help', command = None) 
        self.help_.add_command(label ='Demo', command = None) 
        self.help_.add_separator() 
        self.help_.add_command(label ='About Tk', command = None)
        #display on Window
        self.app_window.config(menu = self.menubar) 

class Win1(View_1):
    def __init__(self, win_manager, New_View):
        if New_View == True:
            View_1.__init__(self, win_manager, "Welcome Window")   
            self.tk.Tk()
            self.setup_new_window()
        else:
            self.app_window = win_manager.check_views(self.App_Name)
            #Checks if App_window is set to string or View
            if self.app_window == "View Not Found":
                View_1.__init__(self, win_manager, "Main View")   
                self.setup_new_window()

    def setup_new_window(self):
        Main_Window(self)
        self.win_manager.add_views(self)
        self.frame = self.tk.Frame(self.app_window, bg="white").grid(row=3, column=3)
        self.create_default_menubars()
        self.show_default_widgets()

class Win2(View_1):
    def __init__(self, win_manager):
        View_1.__init__(self, win_manager, "OS Check")
        self.app_window = win_manager.check_views(self.App_Name)
        #Checks if App_window is set to string or View
        if self.app_window == "View Not Found":
            new_window(self)
            self.win_manager.add_views(self)
            self.OS_Info = win_manager.MVC_App.controller.OS_Model.OS_Info
            self.create_default_menubars()
            self.show_default_widgets()
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
            self.create_default_menubars()
            self.show_default_widgets()
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


# Window Manager Methods
def get_win(win_manager, _view):
    return _view(win_manager)

def initial_view(win_man, _view): 
    return _view(win_man, True)

# Common Window Methods
def Main_Window(_win):
    _win.app_window = tkint.Tk()
    _win.app_window.title(_win.App_Name)
    _win.win_manager.app_window = _win.app_window

def new_window(_win):
    _win.app_window = _win.tk.Toplevel()
    _win.app_window.title(_win.App_Name)
    _win.win_manager.app_window = _win.app_window

def next_view(_win, _App_Name, _view):
    _check = _win.win_manager.add_views(_win)
    #print(_win.App_Name)
    if _check == "View Not Found":       
        _win.win_manager.app_window = _view(_win.win_manager).app_window
    else:
        _win.win_manager.app_window = _check
        
