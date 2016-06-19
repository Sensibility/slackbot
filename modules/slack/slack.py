#!/usr/bin/python
from slacker import Slacker

secretkey = str(open('/etc/slackbot/API').read());
print("secretkey is {0}".format(secretkey));
slack = Slacker(secretkey);

slack.chat.post_message('#general', 'Leif is a big nerd');
