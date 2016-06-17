#!/usr/bin/python
from slacker import Slacker

secretkey = str(open('slackbot/secret.txt').read());

slack = Slacker(secretkey);

#slack.chat.post_message('#general', 'Leif is a big nerd');
