#!/usr/bin/python3
#Initialized Variables

#Variables
PRETTY_NAME = ""
NAME = ""
VERSION_ID = ""
VERSION = ""
VERSION_CODENAME = ""
ID = ""
ID_LIKE = ""
HOME_URL = ""
SUPPORT_URL = ""
BUG_REPORT_URL = ""
# Function Fills in Data
def Fill_Value(Variable_Name, Variable_Value):
	global PRETTY_NAME, NAME, VERSION_ID, VERSION, VERSION_CODENAME, ID, ID_LIKE, HOME_URL, SUPPORT_URL, BUG_REPORT_URL 
	if Variable_Name == "PRETTY_NAME":
		PRETTY_NAME = Variable_Value
	elif Variable_Name == "NAME" :
		NAME = Variable_Value
	elif Variable_Name == "VERSION_ID":
		VERSION_ID = Variable_Value
	elif Variable_Name == "VERSION":
		VERSION = Variable_Value
	elif Variable_Name == "VERSION_CODENAME":
		VERSION_CODENAME = Variable_Value
	elif Variable_Name == "ID":
		ID = Variable_Value
	elif Variable_Name == "ID_LIKE":
		ID_LIKE = Variable_Value
	elif Variable_Name == "HOME_URL":
		HOME_URL = Variable_Value
	elif Variable_Name == "SUPPORT_URL":
		SUPPORT_URL = Variable_Value
	elif Variable_Name == "BUG_REPORT_URL":
		BUG_REPORT_URL = Variable_Value
	else:
		print("Variable Name Mismatch: " + Variable_Name + " " + Variable_Value)
	return 0
# Function Reads OS-Release File
def Make_OSRelease() :
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
				Fill_Value(OSRelease_Data[Variable_Name_Start:Variable_Name_End], OSRelease_Data[Variable_Value_Start:Variable_Value_End] )
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

def Test_OSRelease():
	global PRETTY_NAME, NAME, VERSION_ID, VERSION, VERSION_CODENAME, ID, ID_LIKE, HOME_URL, SUPPORT_URL, BUG_REPORT_URL 
	Make_OSRelease()
	print("PRETTY_NAME = " + PRETTY_NAME)
	print("NAME = " + NAME)
	print("VERSION_ID = " + VERSION_ID)
	print("VERSION = " + VERSION)
	print("VERSION_CODENAME = " + VERSION_CODENAME)
	print("ID = " + ID)
	print("ID_LIKE = " + ID_LIKE)
	print("HOME_URL = " + HOME_URL)
	print("SUPPORT_URL = " + SUPPORT_URL)
	print("BUG_REPORT_URL = " + BUG_REPORT_URL)
	return 0