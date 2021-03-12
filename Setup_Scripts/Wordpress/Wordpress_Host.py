#!/usr/bin/python3

class WP_Host:
    def __init(self, Parent):
        self.Controller = Parent

    def Create_Host(self, Host_Type):
        if Host_Type.Host == "Wordpress":
            self.Controller.WP_Script.subprocess.call("./Wordpress/Wordpress_initialization.sh")