import os.path


#I should probably find a way to utilize these
dota_synonymns=["dota", "Dota", "dota2", "Dota2"]
ow_synonymns=["ow", "overwatch", "Overwatch"]

def patchFetch(args, slackAPI, channel, users):
	if len(args)==0:
		slackAPI.chat.post_message(channel['name'], "Not enough arguments to patch. Usage: `!patch <game>`")
		return "WW: patch: not enough arguments"
	datfile = "/etc/slackbot/modules/patch/"+args[0]
	if os.path.isfile(datfile):
		patchnotes=open('/etc/slackbot/modules/patch/'+args[0]).read()
		slackAPI.chat.post_message(channel['name'], patchnotes, as_user=True, username="patchbot")
		return "II: patch: posted patch notes for "+args[0]
	slackAPI.chat.post_message(channel['name'], "Couldn't find patch notes for '"+args[0]+"'. Either this isn't a real game or @roogz is fucking memeing again.")
	return "WW: patch: patch notes not found for "+args[0]

