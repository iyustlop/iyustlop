import os

class myUser:
	
	def getUser(self):
		return os.environ['usuario']

	def getPassword(self):
		return os.environ['contrasena']

	def getDriver(self):
		return os.environ['mydriver']
	
