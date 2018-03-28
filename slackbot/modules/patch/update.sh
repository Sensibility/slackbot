#!/bin/bash


######################
###      Dota2     ###
######################

#First, get the url of the latest patch
#(last 20 entries should do)
DOTA_UPDATES=$(curl "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=570&count=5&maxlength=300&format=json")

#now get a url
URL=$(python3 /etc/slackbot/modules/patch/steamurl_parse.py pre $DOTA_UPDATES | sed -z 's/\n//g')

python3 /etc/slackbot/modules/patch/steamurl_parse.py post "$(curl $URL | sed -z 's/.*<div class="body">//' | sed -z 's/<div.*//' | sed 's/<br>/\n/g' | sed 's/$/\n/')" > /etc/slackbot/modules/patch/dota

######################
###	   Overwatch   ###
######################
# This is deprecated, for an explanation, check the module docstring in overwatch_parse.py
# OWDATA=$(curl -X GET --header 'Accept: application/json' 'https://api.lootbox.eu/patch_notes')
# python3 /etc/slackbot/modules/patch/overwatch_parse.py post "$(python3 /etc/slackbot/modules/patch/overwatch_parse.py pre $OWDATA | sed 's/<[^>]\+>/ /g')" > /etc/slackbot/modules/patch/overwatch

######################
###  Vermintide 2  ###
######################
# Experimental, uses the dota2 parsing engine
VERMINTIDE_UPDATES=$(curl "https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=552500&count=5&maxlength=300&format=json")

# now get a URL
URL=$(python3 /etc/slackbot/modules/patch/steamurl_parse.py pre $VERMINTIDE_UPDATES | sed -z 's/\n//g')

python3 /etc/slackbot/modules/patch/steamurl_parse.py post $(curl $URL)
