#!/usr/bin/python3

import sys
import json


if sys.argv[1]=="pre":
	updates = json.loads(" ".join(sys.argv[2:]))

	for update in updates['appnews']['newsitems']:
		if update['feedlabel'] == "Product Update":
			print(update['url'])
			break
elif sys.argv[1]=="post":
	prettytext = list(filter(None, " ".join(sys.argv[2:]).strip().split("\n")))
	prettytext = [x.strip() for x in prettytext]
	textBuilder = []
	inList = False
	for line in prettytext:
		formattedLine = line
		if inList == False and line[0] in ["*","-"]:
			inList=True
			formattedLine=">```"+line[1:]+"\n"
		elif inList == True:
			if line[0] in ["*","-"]:
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
	print(prettytext)
