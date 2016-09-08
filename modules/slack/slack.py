#!/usr/bin/python
from slacker import Slacker
<<<<<<< HEAD
import baseModule
=======

>>>>>>> 6088d7b12210e3a3d1b9da9cffab955da54863a7
secretkey = str(open('/etc/slackbot/API').read());
print("secretkey is {0}".format(secretkey));
slack = Slacker(secretkey);

slack.chat.post_message('#general', 'Leif is a big nerd');
<<<<<<< HEAD

class Slacker(Module):
	def __init__(self, paths):
		self.__super__()
		self.paths = paths

		self.secrets()
#		print paths

	def processSetings(self, data):
		print(data)

	def secrets(self):
		print("Secrets")
=======
>>>>>>> 6088d7b12210e3a3d1b9da9cffab955da54863a7
