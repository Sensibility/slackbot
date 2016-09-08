#!/usr/bin/python
from slacker import Slacker
import baseModule
secretkey = str(open('/etc/slackbot/API').read());
print("secretkey is {0}".format(secretkey));
slack = Slacker(secretkey);

slack.chat.post_message('#general', 'Leif is a big nerd');

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
