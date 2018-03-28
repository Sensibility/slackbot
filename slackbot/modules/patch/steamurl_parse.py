#!/usr/bin/python3
"""
This module parses dota2 patch notes, and prints them to stdout
"""

import sys
import json

# pre-processing mode: gets a url for the update from the raw steam post, 
# which is then `curl`d back into this script for post-processing.
if sys.argv[1]=="pre":
	updates = json.loads(" ".join(sys.argv[2:]))
	for update in updates['appnews']['newsitems']:
		if update['feedlabel'] == "Product Update":
			print(update['url'])
			exit()

	# If we didn't find any "Product Update"s, we'll try to parse something else.
	# For vermintide in particular, this works if we check "Community Announcement"s
	# for titles that include "Patch"
	for update in updates['appnews']['newsitems']:
		if update['feedlabel'] == "Community Announcements" and "Patch" in update['title']:
			if update['is_external_url']:
				print("http://steamcommunity.com/games/%s/announcements/detail/%s" % (update['appid'], update['gid']))
			else:
				print(update['url'])
			exit()



# post-processing mode: takes the html of a steam update and formats it in slack-supported
# markdown. Prints the results on stdout
elif sys.argv[1]=="post":
	# Read in the page and split it into non-empty, non-whitespace lines
	prettytext = sys.stdin.read().strip().split("\n")
	prettytext = [x.strip() for x in prettytext if x and x.strip()]


	textBuilder = []
	inList = False # keeps track of whether or not we are in a list
	for line in prettytext:
		formattedLine = line

		# This line is the start of a list
		if not inList and line[0] in {"*", "-"}:
			inList = True
			formattedLine = ">```" + line[1:]

		# We're already in a list
		elif inList:

			# This is another item in the list
			if line[0] in {"*", "-"}:
				formattedLine = line[1:]

			# This item isn't in the list; so this is the end of the list
			else:
				inList = False
				if line == "HEROES" or line == "ITEMS":
					formattedLine = "```\n\n*%s*" % line
				else:
					formattedLine = "```\n_%s_" % line

		# Section titles
		elif "Gameplay Update" in line:
			formattedLine = "*_%s_*" % line
		elif line == "HEROES" or line == "ITEMS":
			formattedLine = "*%s*" % line
		else:
			formattedLine = "_%s_" % line

		# Append the result
		textBuilder.append(formattedLine)

	# If at the end of the patch, we're still in a list, end the list
	if inList:
		textBuilder.append("```")

	# print the output
	prettytext = '\n'.join(textBuilder)
	print(prettytext)
