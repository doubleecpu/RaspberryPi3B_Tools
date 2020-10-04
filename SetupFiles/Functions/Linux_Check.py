import sys
from .Linux_OS_Release import OS_Release

class CheckOS:
    def __init__(self):
        self.OSRelease = OS_Release() 
        self.CurrentOS = sys.platform

    #return super().__init__(*args, **kwargs)

    def Check_SW(self):
        print("System is running " + sys.platform)
        print("Checking Version of Linux")
        self.OSRelease.Make_OSRelease()
        ID = self.OSRelease.VERSION_ID[1:2]
        if int(ID) < 8 : 
            print("Linux Version ok")
        else:
            print("Linux Version Older than version 8 Currently: " + self.OSRelease.VERSION )
        return 0 