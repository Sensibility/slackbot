import os.path

dota_synonymns=["dota", "Dota", "dota2", "Dota2"]
ow_synonymns=["ow", "overwatch", "Overwatch"]


#applies any applicable beautification to patch text
def formatNotes(notes, game):

	#dota patch beautification
	if game in dota_synonymns:
		prettytext = list(filter(None, notes.strip().split("\n")))
		prettytext = [x.strip() for x in prettytext]
		textBuilder = []
		inList = False
		for line in prettytext:
			formattedLine = line
			if inList == False and line[0] == "*":
				inList=True
				formattedLine=">```"+line[1:]+"\n"
			elif inList == True:
				if line[0] == "*":
					formattedLine = line[1:]+"\n"
				else:
					inList=False
					if line == "HEROES" or line == "ITEMS":
						formattedLine = "```\n\n*"+line+"*\n"
					else:
						formattedLine = "```\n_"+line+"_\n"
			elif "Gameplay Update" in line:
				formattedLine = "*_"+line+"_*\n"
			elif line == "HEROES" or line == "ITEMS":
				formattedLine = "\n*"+line+"*\n"
			else:
				formattedLine = "_"+line+"_\n"
			textBuilder.append(formattedLine)
		if inList:
			textBuilder.append("```")
		prettytext="".join(textBuilder)
		return prettytext

	#Overwatch patch beautification
	elif game in ow_synonymns:
		prettytext=notes.strip().split("\n")
		prettytext=[x.strip() for x in prettytext]
		prettytext=list(filter(None, prettytext))
		textBuilder=[]
		inList=False
		for line in prettytext:
			formattedLine = line
			if line[0:8] == "Version ":
				formattedLine = "*_"+line+"_*\n"
			elif "UPDATES" in line or "BUG FIXES" == line:
				if inList:
					inList=False
					formattedLine="```\n*"+line+"*\n"
				else:
					formattedLine="\n*_"+line+"_*\n"
			elif "Heroes" == line or "General" == line or "Maps" == line: 
				if inList:
					formattedLine = "```\n_"+line+"_\n"
					inList=False
				else:
					formattedLine = "\n_"+line+"_\n"
			elif not inList:
				formattedLine = ">```"+line+"\n"
				inList = True
			else:
				formattedLine += "\n"
			textBuilder.append(formattedLine)
		if inList:
			textBuilder.append("```")
		return "".join(textBuilder)
	else:
		return notes;

def patchFetch(args, slackAPI, channel):
	if len(args)==0:
		return "EE: patch: not enough arguments"
	datfile = "/etc/slackbot/modules/patch/"+args[0]
	if os.path.isfile(datfile):
		patchnotes=open('/etc/slackbot/modules/patch/'+args[0]).read()
		formattedText = formatNotes(patchnotes, args[0])
		slackAPI.chat.post_message(channel['name'], formattedText, as_user=True, username="patchbot")
		return "II: patch: posted patch notes for "+args[0]
	slackAPI.chat.post_message(channel['name'], "Couldn't find patch notes for '"+args[0]+"'. Either this isn't a real game or @roogz is fucking memeing again.")
	return "EE: patch: patch notes not found for "+args[0]

