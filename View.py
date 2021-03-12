#!/usr/bin/python3

from SetupFiles.Views import Linux_View as Views

class Window_Manager:
    def __init__(self, parent):
        #reference main App
        print("- Starting GUI") 
        self.MVC_App = parent.MVC_App
        self.App_sys = parent.App_sys
        self.App_Name = "Window_Manager"
        #setup main window for Sensors App
        self.LARGE_FONT= ("Verdana", 10)
        self.views_List = []
        #sets up the first window to appear
        self.app_window = Views.initial_view(self, Views.Win1)

    def check_views(self, view_name):
        if self.views_List is None:
            return "View Not Found"
        else:
            print(f"looking for View:", view_name)
            for obj in range(len(self.views_List)):
                print("View in List:", self.views_List[obj].App_Name)
                if self.views_List[obj].App_Name == view_name:
                    print("Found Existing View:", view_name)
                    return self.views_List[obj]
            print("Not Found")
            return "View Not Found"
                  

    def add_views(self, view_win_):
        print("Adding View to List")
        print(view_win_.App_Name)
        self.views_List.append(view_win_)

    def remove_view(self, view_win_):
        _check = self.check_views(view_win_.App_Name) 
        if _check != "View Not Found":
            self.views_List.remove(view_win_)

    def close_views(self):
         for obj in range(len(self.views_List)):
            print("closing", self.views_List[obj].App_Name)
            self.views_List[obj].app_window.destroy()
            
         self.views_List = None
         self.App_sys.exit(0)

    def view_loop(self):
        #The Sensors App Window Appear
        self.app_window.Linux_View_loop()