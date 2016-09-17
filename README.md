# Slackbot
A multi-use extensible bot for the slack api (based on the 'Slacker' slack api implementation)
Passes commands to separate "modules" for appropriate handling.

Currently, the following two modules are installed:

##LaTeX
This module parses the remainder of any command entered that is prefaced with `!math`
e.g. `!math $\int_a^b\frac{\mathrm{d}{\mathrm{d}y}x^2dx$ will output the following:
![screen]
It can be used to parse (somewhat) arbitrary fragments of latex code, not just math,
though that is its primary use.

##patch
This module fetches patch notes for the latest patch of a specified game. For example,
`!patch dota` will fetch the latest Dota2 patch. Currently only dota and overwatch patch
notes are fetchable.

##How to use:
This bot has _ONLY_ been tested on Linux (Mint 17 and Ubuntu 15) and will _NOT_ work
on Windows. It may be possible to run on Mac, but could require some fiddling.
Install from the downloaded directory using:
```
root@machine~# ./install.sh
```
Pass the api token directly to the install script via `-a` or `-A`, or put it in `/etc/slackbot/API`.

Start bot by running `# service slackbot start` or `# /var/www/slackbot/botd` (the first
command allows `systemd` to manage the daemon, if `systemd` is not present on your server
or you simply do not wish to use it, the script may be run manually by the second command,
storing its pid in `/var/run/slackbot.pid`)


[screen]:http://i.imgur.com/7xbkJ6P.png
