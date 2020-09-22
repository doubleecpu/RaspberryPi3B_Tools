#!/usr/bin/python3
#Initialized Variables

#Variables
class OS_Release:
    def __init__(self):
        self.PRETTY_NAME = ""
        self.NAME = ""
        self.VERSION_ID = ""
        self.VERSION = ""
        self.VERSION_CODENAME = ""
        self.ID = ""
        self.ID_LIKE = ""
        self.HOME_URL = ""
        self.SUPPORT_URL = ""
        self.BUG_REPORT_URL = ""
# Function Fills in Data
    def Fill_Value(self, Variable_Name, Variable_Value):
        if Variable_Name == "PRETTY_NAME":
            self.PRETTY_NAME = Variable_Value
        elif Variable_Name == "NAME" :
            self.NAME = Variable_Value
        elif Variable_Name == "VERSION_ID":
            self.VERSION_ID = Variable_Value
        elif Variable_Name == "VERSION":
            self.VERSION = Variable_Value
        elif Variable_Name == "VERSION_CODENAME":
            self.VERSION_CODENAME = Variable_Value
        elif Variable_Name == "ID":
            self.ID = Variable_Value
        elif Variable_Name == "ID_LIKE":
            self.ID_LIKE = Variable_Value
        elif Variable_Name == "HOME_URL":
            self.HOME_URL = Variable_Value
        elif Variable_Name == "SUPPORT_URL":
            self.SUPPORT_URL = Variable_Value
        elif Variable_Name == "BUG_REPORT_URL":
            self.BUG_REPORT_URL = Variable_Value
        else:
            print("Variable Name Mismatch: " + Variable_Name + " " + Variable_Value)
        return 0
# Function Reads OS-Release File
    def Make_OSRelease(self) :
        # Open os-release file
        OSRelease_file = open("/etc/os-release")
        OSRelease_Data = OSRelease_file.read()
        TextLength = len(OSRelease_Data)
        print("File has " + str(TextLength) + " characters")
        # Initializes Position Markers
        Current_Position = 0
        Variable_Name_Start = 0 
        Variable_Name_End = 0
        Variable_Value_Start = 0
        Variable_Value_End =0 
        Name_And_Value = False
        if OSRelease_Data[Current_Position:1] == "":
            print("Reached End Of File")
        else :
            print( len(OSRelease_Data))
            for Current_Position in range(len(OSRelease_Data)):
                if Name_And_Value == True :
                    self.Fill_Value(OSRelease_Data[Variable_Name_Start:Variable_Name_End], OSRelease_Data[Variable_Value_Start:Variable_Value_End] )
                    Variable_Name_Start = Current_Position 
                    Name_And_Value = False
                else : 
                    if OSRelease_Data[Current_Position] == "=" :
                        Variable_Name_End = Current_Position 
                        Variable_Value_Start = Current_Position + 1
                    elif (OSRelease_Data[Current_Position] == "\n"):
                        Variable_Value_End = Current_Position 
                        Name_And_Value = True
                    elif OSRelease_Data[Current_Position] == "\r":
                        Variable_Value_End = Current_Position 
                        Name_And_Value = True 
                    # End IF
                #End IF
            # For Loop
        # End IF
        return 0

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

    
Test1 = Test_OSRelease(OS_Release())
Test1.Test_OS()