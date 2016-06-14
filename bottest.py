#!/usr/bin/python

from slacker import Slacker

secretkey = open('secret.txt').read();

print(secretkey);

slack = Slacker('this is a stub, reading it from a file is giving format errors');

slack.chat.post_message('#general', 'Leif is a big nerd');
