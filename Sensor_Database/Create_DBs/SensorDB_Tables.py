#!/usr/bin/python
from subprocess import call

print("Creating SensorDB")
bashCall = call("./Create_SensorDB.sh")
print("Created SensorDB")
