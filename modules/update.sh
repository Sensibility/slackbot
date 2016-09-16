#!/bin/bash

#First, get the url of the latest patch
#(last 20 entries should do)
UPDATES=$(curl "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=570&count=5&maxlength=300&format=json")

#now get a url
URL=$(/usr/bin/python3 /etc/slackbot/modules/patch/steamurl_parse.py $UPDATES | sed -z 's/\n//g')

curl $URL | sed -z 's/.*<div class="body">//' | sed -z 's/<div.*//' | sed 's/<br>/\n/g' | sed 's/$/\n/' > /etc/slackbot/modules/patch/dota
