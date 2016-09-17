#!/usr/bin/python3
#This file parses commands for
#the Sensibot daemon, then runs
#the appropriate function

#fetches patch information
from modules.patch.patch import *
from modules.math.math import uploadLatex

#use this to add functions to call
commands = {'!patch': patchFetch,
			'!math': uploadLatex,
			'!latex': uploadLatex}



def parseMessage(message, slackAPI, channel, users):
	args = message['text'].split(" ")
	possible_command = args.pop(0)
	if possible_command in commands:
		return commands[possible_command](args,slackAPI,channel,users)
