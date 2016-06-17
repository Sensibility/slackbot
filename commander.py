import json
from pprint import pprint

class Commander():
	def __init__(self, settingsFile = 'settings.json'):
		with open(settingsFile) as settings:
			self.settings = json.load(settings)

		self.processSettings()

	#Loop over all of the settings and perform any necesary actions
	def processSettings(self):
		for setting in self.settings:
			if(setting == 'modules'):
				self.processModules()

	#Start all of the modules that are activated
	def processModules(self):
		for module in self.settings['modules']:
			print(module)



if __name__ == "__main__":
	com = Commander()