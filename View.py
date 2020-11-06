#!/usr/bin/env python3  

from SetupFiles.Views import Linux_View as Views


class Window_Manager:
    def __init__(self, parent):
        #reference main App
        print("- Starting GUI") 
        self.MVC_App = parent.MVC_App
        self.App_Name = "Window_Manager"
        #setup main window for Sensors App
        self.LARGE_FONT= ("Verdana", 10)
        self.views_List = []
        #sets up the first window to appear
        self.app_window = Views.initial_view(self, Views.Win1)

    def check_views(self, view_name):
        view_obj = None 
        for obj in self.views_List:
            if obj.App_Name == view_name:
                view_obj = obj
        if view_obj is None:
            view_obj = str("View Not Found")
        return view_obj

    def add_views(self, view_win_):
        _check = self.check_views(view_win_.App_Name) 
        if _check == "View Not Found":
            self.views_List.append(view_win_)

    def remove_view(self, view_win_):
        _check = self.check_views(view_win_.App_Name) 
        if _check != "View Not Found":
            self.views_List.remove(view_win_)

    def mainloop(self):
        #The Sensors App Window Appear
        self.app_window.tk.mainloop()