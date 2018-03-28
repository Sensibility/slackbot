#!/usr/bin/python3

"""
This module used to parse patch notes for Overwatch back in the day,
but Blizzard is dumb so they don't host their own patch note API, and
the free and open source one that I used to use is no longer online.
I'm leaving this here in case it's ever useful, but it's doubtful.
"""

import sys
import json

if sys.argv[1] == "pre":
	patch=json.loads(" ".join(sys.argv[2:]))['patchNotes'][0]
	output=patch['patchVersion']
	rawhtml=patch['detail']
	print("Version "+output+"\n"+rawhtml)
elif sys.argv[1] == "post":
	prettytext=" ".join(sys.argv[2:]).strip().split("\n")
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
	print("".join(textBuilder))
