#!/usr/bin/python3
#This file parses commands for
#the Sensibot daemon, then runs
#the appropriate function

#fetches patch information
from modules.patch.patch import *
from modules.math.math import uploadLatex
from modules.recipe.recipe import *

import slacker
import typing

#use this to add functions to call
commands = {'!patch': patchFetch,
			'!math': uploadLatex,
			'!latex': uploadLatex,
			'!recipe': fetchRecipiesByQuery,
			'!recipeI': fetchRecipiesByIngredients}



def parseMessage(message: object,
                 slackAPI: slacker.Slacker,
                 channel: object,
                 users: typing.List[object]) -> typing.Optional[str]:
	"""
	Gets the name of a command from the text in a message.

	Returns the output (if any) from the command, to be logged by the bot.
	"""
	args = message['text'].split(" ")
	possibleCommand = args.pop(0)
	if possibleCommand in commands:
		return commands[possibleCommand](args, slackAPI, channel, users)
