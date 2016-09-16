#!/usr/bin/python3
#This file parses commands for
#the Sensibot daemon, then runs
#the appropriate function

#fetches patch information
from modules.patch.patch import *

#use this to add functions to call
commands = {'!patch': patchFetch}



def parseMessage(message, slackAPI, channel):
	args = message['text'].split(" ")
	possible_command = args.pop(0)
	if possible_command in commands:
		return commands[possible_command](args,slackAPI,channel)