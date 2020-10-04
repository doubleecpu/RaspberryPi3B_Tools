 from ..SetupFiles.Functions import Linux_OS_Release, Linux_Check, SW_Check

 class Test_OSRelease:
    def __init__(self, OS_Release):
        self.OS_Info = OS_Release
        self.OS_Info.Make_OSRelease()

    def Test_OS(self):
        print("PRETTY_NAME = " + self.OS_Info.PRETTY_NAME)
        print("NAME = " + self.OS_Info.NAME)
        print("VERSION_ID = " + self.OS_Info.VERSION_ID)
        print("VERSION = " + self.OS_Info.VERSION)
        print("VERSION_CODENAME = " + self.OS_Info.VERSION_CODENAME)
        print("ID = " + self.OS_Info.ID)
        print("ID_LIKE = " + self.OS_Info.ID_LIKE)
        print("HOME_URL = " + self.OS_Info.HOME_URL)
        print("SUPPORT_URL = " + self.OS_Info.SUPPORT_URL)
        print("BUG_REPORT_URL = " + self.OS_Info.BUG_REPORT_URL)