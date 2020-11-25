#!/usr/bin/python3

class Bash_DB:
    def __init(self, Parent):
        self.Controller = Parent

    def Create_DB(self, DB_Type):
        if DB_Type == "LAMP":
            self.Controller.subprocess.call("./LAMP_Setup.sh")
