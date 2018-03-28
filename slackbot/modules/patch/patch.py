"""
This module checks for the name of a supported game in the arguments to the api command, and
if found it reads the latest patch, printing it to the channel in which it was requested.
"""

import os.path
import typing

#I should probably find a way to utilize these
dota_synonymns=["dota", "Dota", "dota2", "Dota2"]
ow_synonymns=["ow", "overwatch", "Overwatch"]

def patchFetch(args: typing.List[str], slackAPI: object, channel: object, users: list) -> str:
	"""
	Fetches th epatch notes for the appropriate game, and posts it to the channel.
	"""

	# If there isn't a game name, print and log an error
	if len(args) == 0:
		slackAPI.chat.post_message(channel['name'], "Not enough arguments to `!patch`. Usage: `!patch <game>`")
		return "WW: patch: not enough arguments"

	# Read in the patch notes from the file if it exists
	datfile = "/etc/slackbot/modules/patch/" + args[0]
	if os.path.isfile(datfile):
		patchnotes = open('/etc/slackbot/modules/patch/'+args[0]).read()
		slackAPI.chat.post_message(channel['name'], patchnotes, as_user=True, username="patchbot")
		return "II: patch: posted patch notes for "+args[0]

	# If patch notes are not found, post and log an error message
	slackAPI.chat.post_message(channel['name'], "Couldn't find patch notes for '%s'."\
	                                            "Either this isn't a real game or"\
	                                            "@roogz is fucking memeing again." % args[0])
	return "WW: patch: patch notes not found for "+args[0]

