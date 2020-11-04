#!/usr/bin/env python3

from  tkinter import * 

class Win1:
    def __init__(self, win_manager):
        #self.i_tk = i_tk
        self.App_Name = "Win1"
        self.MVC_App = win_manager.MVC_App
        self.main_window = win_manager.main_window
        self.frame = Frame(self.main_window, bg="red")
        self.frame.grid(row=3, column=3)
        win_manager.show_widgets()


class Win2:
    def __init__(self, win_manager):
        self.win_manager = win_manager
        self.main_window = win_manager.main_window
        self.App_Name = "Win2"
        self.frame = win_manager.frame
        self.OS_Info = win_manager.MVC_App.controller.OS_Model.OS_Info
        self.win_manager.show_widgets()
        self.win_manager.create_menubars
        self.show_widgets()

    def show_widgets(self):
        "List of Data gathered about OS"
        self.frame = Frame(self.main_window, bg="red")
        self.quit_button = Button(self.frame, text=f"Close OS Information", command=self.close_window)
        self.quit_button.grid(row=2, column=3)
        self.label_PRETTY_NAME = Label(self.frame, text=self.OS_Info.PRETTY_NAME,font=self.win_manager.LARGE_FONT, bg="green")
        self.label_PRETTY_NAME.grid(row=2, column=2)
        #self.NAME = ""
        #self.VERSION_ID = ""
        #self.VERSION = ""
        #self.VERSION_CODENAME = ""
        #self.ID = ""
        #self.ID_LIKE = ""
        #self.HOME_URL = ""
        #self.SUPPORT_URL = ""
        #self.BUG_REPORT_URL = ""
        self.quit = Button(self.frame, text=f"Quit this window n. 3", command=self.close_window)

    def close_window(self):
        self.main_window.destroy()

class Win3:
    def __init__(self, win_manager):
        #Close Current Window
        self.main_window = win_manager.main_window
        self.close_window()
        #Open New Window
        self.main_window = Tk()
        self.App_Name = "Win3"
        self.frame = win_manager.frame
        print(win_manager.App_Name)
        #Setup Window
        win_manager.show_widgets()
        win_manager.show_menubars()
        self.show_widgets()


    def show_widgets(self):
        #self.frame = Frame(self.main_window, bg="green")
        self.quit = Button(self.frame, text=f"Quit this window n. 3", command=self.close_window)
        self.quit.grid(row=2, column=3)
        self.label = Label(self.frame, text="THIS IS ONLY IN THE THIRD WINDOW")
        self.label.grid(row=1, column=1)

    def close_window(self):
        self.main_window.destroy()

def get_win(self, win_manager, _class):
    win_manager.App_window = _class(win_manager)
