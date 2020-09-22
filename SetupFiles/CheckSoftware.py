
import sys; 
import os;
from Functions import ReadOSRelease

OS = ReadOSRelease.OS_Release()

def Check_SW():
    print("System is running " + sys.platform)
    print("Checking Version of Linux")
    ReadOSRelease.Make_OSRelease()
    if int(ReadOSRelease.VERSION_ID) > 8 : 
        print("Linux Version ok")
    else:
        print("Linux Version Older than version 8 Currently: " + ReadOSRelease.VERSION )

    print( "Checking Version Python")

    print ("Python3 version is: " + sys.version)

    print( "Checking Version GPIO")

    print( "Checking Version I2C")

    print( "Checking Version SPI")

    print( "Checking Version UART")

    print( "Checking MySQL")

    print( "Checking Apache")

    print( "Checking PHP")

    print( "Checking NodeJS")

    print( "Checking Wordpress")

    print( "Finished Checking Software")

    return 0

Check_SW