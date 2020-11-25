#!/usr/bin/python3

class Bash_DB:
    def __init(self, Parent):
        self.Controller = Parent

    def Create_DB(self, DB_Type):
        if DB_Type.DB_Stack == "LAMP":
            self.Controller.Bash_Script.subprocess.call("./Sensor_Database/LAMP_Server/LAMP_Setup.sh")
