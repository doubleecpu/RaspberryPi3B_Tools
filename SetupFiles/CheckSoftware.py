from Functions import Linux_Check, SW_Check

def get_Available_SW():
    print("Checking Software Available on System")
    SW = Linux_Check.CheckOS()
#    SW.OSRelease.Make_OSRelease()
    if SW.CurrentOS == "linux" :
        print("- Linux Version is: " + SW.OSRelease.ID)
        print("Checking Installed SW") 
        SW = SW_Check.SW_Installed()
        SW.Print_Values()


get_Available_SW()