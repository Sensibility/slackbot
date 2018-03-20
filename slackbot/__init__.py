#!/usr/bin/python3

from slacker import Slacker

from pwd import getpwnam

from commander import *

print("Slackbot starting up... ");

slackbot = Slacker(open('/etc/slackbot/API').read().strip());

users = slackbot.users.list().body['members']

listenChannels = []
lastheard = dict()

for channel in slackbot.channels.list().body['channels']:
	if channel['is_member']:
		listenChannels.append(channel)
		lastheard[channel['id']] = -1.0

while(True):
	for channel in listenChannels:
		chat_hist = slackbot.channels.history(channel['id']).body['messages']
		for message in chat_hist:
			if "bot_id" in message:
				continue
			if lastheard[channel['id']] == float(message['ts']):
				break
			if 'text' in message:
				if lastheard[channel['id']] > float(message['ts']):
					continue
				lastheard[channel['id']] = float(message['ts'])
				response = parseMessage(message, slackbot, channel, users)
				if response != None:
					print(response)
