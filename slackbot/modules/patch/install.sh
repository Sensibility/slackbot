#!/bin/sh

crontab patch_crontab

mkdir -p /var/www/slackbot/modules/patch
cp __init__.py /var/www/slackbot/modules/patch/
mkdir -p /etc/slackbot/modules/patch
cp patch.py /var/www/slackbot/modules/patch/
cp update.sh /etc/slackbot/modules/patch/
cp steamurl_parse.py /etc/slackbot/modules/patch/
cp overwatch_parse.py /etc/slackbot/modules/patch/

/etc/slackbot/modules/patch/update.sh