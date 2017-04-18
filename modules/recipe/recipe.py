#!/usr/bin/python3

import urllib.request
import json

msg_header = "Recipies fetched by recipepuppy.com (he's a good pupper)\n"

def fetchRecipiesByQuery(args, slackAPI, channel, users):
	url = "http://www.recipepuppy.com/api/?q="
	url+=",".join(args)
	return fetchRecipies(slackAPI, channel, url)

def fetchRecipiesByIngredients(args, slackAPI, channel, users):
	url = "http://www.recipepuppy.com/api/?i="
	url += ",".join(args)
	return fetchRecipies(slackAPI, channel, url)

def fetchRecipies(slackAPI, channel, url):
	response = urllib.request.urlopen(url)
	if response.code != 200:
		slackAPI.chat.post_message(channel['name'], "Couldn't fetch recipies for the given url: '"+url+"'")
		return "EE: recipe: unable to connect to recipepuppy api, return code: "+str(response.code)
	resp_str = response.read().decode()
	recipies_response=json.loads(resp_str)
	msg = []
	for recipe in recipies_response['results']:
		recipe_str="*"+recipe['title']+"*: "+recipe['href']+"\n"+recipe['thumbnail']+"\n"
		ingredients = recipe['ingredients'].split(", ")
		recipe_str+=">```"
		for ingredient in ingredients:
			recipe_str+=ingredient+"\n"
		recipe_str+="```"
		msg.append(recipe_str)
	slackAPI.chat.post_message(channel['name'], msg_header)
	for message in msg:
		slackAPI.chat.post_message(channel['name'],message)
	return "II: recipe: posted "+str(len(msg))+" recipies for query '"+url+"'"