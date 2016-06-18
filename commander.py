import json

class Commander():
	def __init__(self, settingsFile = 'settings.json'):
		self.setDefaults()

		with open(settingsFile) as settings:
			self.settings = json.load(settings)

		self.processSettings()

	#Setting the default settings for if nothing special was specified in the
	#settings.json file
	def setDefaults(self):
		self.corePath = "./core/"
		self.modulesPath = "./modules/"
		self.secretsPath = "./secrets.json"

	#Loop over all of the settings and perform any necesary actions
	def processSettings(self):
		for setting in self.settings:
			if(setting == 'modules'):
				self.processModules()
			elif(setting == 'paths'):
				self.processPaths()

	#Detect all of the modules that are activated, we will start them when the
	#entire settings file has been read in
	def processModules(self):
		for module in self.settings['modules']:
			if(module == "mumble"):
				self.processMumble()

	#Detect all of the paths to various files such as the secrets file and where
	#the core and modules are
	def processPaths(self):
		for path in self.settings['paths']:
			if(path == 'secrets'):
				self.secretsPath = self.settings['paths'][path]
			elif(path == 'core'):
				self.corePath = self.settings['paths'][path]
			elif(path == 'modules'):
				self.modulesPath = self.settings['paths'][path]

	#Process the mumble module and all of it's features
	def processMumble(self):
		print('mumble')
		for moduleSetting in self.settings['modules']['mumble']:
			if(moduleSetting in ['admins', 'moderators']):
				for adMod in self.settings['modules']['mumble'][moduleSetting]:
					print("admin/moderator: " + str(self.settings['modules']['mumble'][moduleSetting]))



if __name__ == "__main__":
	com = Commander()