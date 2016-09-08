class Module:
	def __init__(self):
		print("here")

	#Processes settings.json for each module
	#data contains the settings contained in settings.json
	#Every module must override this function
	def processSettings(self, data):
		raise NotImplementedError("All modules must override this method!!!!")

	#Each process must read in it's secrets
	def secrets(self):
		raise NotImplementedError("All moduels must override this method!!!!")
