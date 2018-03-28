#!/usr/bin/python3
"""
This package contains all the functionality necessary to create a slack chatbot.
"""


def main() -> int:
	"""
	Starts up the slackbot, initializing any installed extension modules.
	"""
	import sys
	import slacker
	from . import commander

	print("Slackbot starting up... ");

	try:
		slackbot = slacker.Slacker(open('/etc/slackbot/API').read().strip());
	except OSError as e:
		print("Could not read API token file: %s" % e, file=sys.stderr)
		return 1

	users = slackbot.users.list().body['members']

	listenChannels = []
	lastheard = {}

	for channel in slackbot.channels.list().body['channels']:
		if channel['is_member']:
			listenChannels.append(channel)
			lastheard[channel['id']] = -1.0

	while(True):
		for channel in listenChannels:
			chat_hist = slackbot.channels.history(channel['id']).body['messages']
			for message in chat_hist:
				if lastheard[channel['id']] == float(message['ts']):
					break
				if "bot_id" not in message and 'text' in message:
					ts = float(message['ts'])
					if lastheard[channel['id']] <= ts:
						lastheard[channel['id']] = ts
						response = commander.parseMessage(message, slackbot, channel, users)
						if response != None:
							print(response)

if __name__ == '__main__':
	exit(main())
