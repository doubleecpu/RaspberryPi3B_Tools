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
        self.Make_OSRelease()
# Function Fills in Data
    def Fill_Value(self, Variable_Name, Variable_Value):
        # debug 
        # print("Variable: " + Variable_Name + " " + Variable_Value)
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

