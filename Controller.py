#!/usr/bin/env python3
# Controls how Data is to be displayed on the app

from Model import Model_OSRelease
from View import Window_Manager

class Control_View:
	def __init__(self, parent):
		self.MVC_App = parent.app
		self.App_Name = "Control_View"
		parent.controller = self
		# creates OS Data Using Functions  
		self.OS_Model = Model_OSRelease(self)
		#self.OS_Model.Test_OS()

		# Creates Windows To Hold OS Data
		self.app = Window_Manager(self)
		self.app.mainloop()
