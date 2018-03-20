#!/bin/bash


######################
###      Dota2     ###
######################

#First, get the url of the latest patch
#(last 20 entries should do)
UPDATES=$(curl "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=570&count=5&maxlength=300&format=json")

#now get a url
URL=$(python3 /etc/slackbot/modules/patch/steamurl_parse.py pre $UPDATES | sed -z 's/\n//g')

python3 /etc/slackbot/modules/patch/steamurl_parse.py post "$(curl $URL | sed -z 's/.*<div class="body">//' | sed -z 's/<div.*//' | sed 's/<br>/\n/g' | sed 's/$/\n/')" > /etc/slackbot/modules/patch/dota

######################
###	   Overwatch   ###
######################
OWDATA=$(curl -X GET --header 'Accept: application/json' 'https://api.lootbox.eu/patch_notes')
python3 /etc/slackbot/modules/patch/overwatch_parse.py post "$(python3 /etc/slackbot/modules/patch/overwatch_parse.py pre $OWDATA | sed 's/<[^>]\+>/ /g')" > /etc/slackbot/modules/patch/overwatch