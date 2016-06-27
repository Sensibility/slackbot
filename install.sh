#!/bin/sh

#Command-line options
IFLAG='f'
SFLAG='f'

#get options
while getopts a:A:his option
do	case "$option" in
	a)
		APIKEY=$OPTARG
		;;
	A)
		APIKEY=$(cat $OPTARG)
		;;
	h)
		echo "Usage: install.sh [-his] [-a <api-key>] [-A <api-key file>]"
		echo "======= Options ========"
		echo "a : Specify your slack api token for setup."
		echo "A : Specify a file containing your api token for setup"
		echo "h : Display this help text and exit."
		echo "i : Install dependancies (will attempt to determine your package manager if necessary, but yum is NOT supported)."
		echo "s : systemd-less install (bot daemon will be placed in /var/www/botd)."
		exit 0
		;;
	i)
		IFLAG='t'
		;;
	s)
		SFLAG='t'
		;;
	[?])
		echo "Try 'install.sh -h' for help"
		exit 1
		;;
	esac
done

#check for proper permissions
if [ $(id -u) -ne 0 ]
then
	if [ $DISPLAY ] && [ $(which gksudo) ]
	then
		gksudo "$0"
		exit 0
	fi
	if [ $(which sudo) ]
	then
		sudo "$0"
		exit 0
	fi
	echo "This script must be run with root permissions, and you don't appear to have sudo so we can't do it ourselves"
	exit 2
fi


#if -i is specified, we must find a package manager
if [ $(which apt-get) ]
then
	PKG='apt'
elif [ $(which pacman) ]
then
	PKG='pac'
else
	echo "-i option was specified, but a suitable package manager could not be found."
	echo "Either install dependancies manually, or continue without the -i option."
	exit 4
fi
	


echo "Checking for dependancies..."

#####################################
###	CHECK FOR DEPENDANCIES    ###
#####################################

#$PATH/python -> */python3
if [ ! $(which python) ]
then
	if [ $(which python3) ]
	then
		ln -s /usr/bin/python $(which python3)
	elif [ $IFLAG = 'f' ]
	then
		echo "You do not appear to have python in your `$PATH`, if you would like us to try to install it run 'install.sh -i', otherwise you must either install it yourself or ensure that it is in your `$PATH`."
		exit 3
	elif [ $PKG = 'apt' ]
	then
		apt-get install python3 && ln -s /usr/bin/python /usr/bin/python3
	elif [ $PKG = 'pac' ]
	then
		pacman -S python3 && ln -s /usr/bin/python /usr/bin/python3
	fi
fi

echo "\tPython found..."


#python is version 3+
if [ $(python --version | sed 's/.*\s//' | sed 's/\..*//') != 3 ]
then
	if [ $IFLAG = 't' ]
	then
		echo "CAUTION: /usr/bin/python is being made a symlink to python3, if this was previously a symlink to python2 some of your scripts may break."
		if [ $(which python3) ]
		then
			ln -s /usr/bin/python $(which python3)
		elif [ $PKG = 'apt' ]
		then
			apt-get install python3 && ln -s /usr/bin/python /usr/bin/python3
		elif [ $PKG = 'pac' ]
		then
			pacman -S python3 && ln -s /usr/bin/python /usr/bin/python3
		fi
	else
		echo "Python is not version 3+, you must link /usr/bin/python to a python3 executable, install python3 and then link, or use the '-i' option."
		exit 3
	fi
fi

echo "\tPython is version 3+..."


#pip is version 3+
if [ ! $(which pip3) ]
then
	if [ $IFLAG = 't' ]
	then
		if [ $PKG = 'apt' ]
		then
			apt-get install python-pip3
		elif [ $PKG = 'pac' ]
		then
			pacman -S python-pip3
		fi
	else
		echo "Pip version 3+ could not be found, you must install pip3 or use the '-i' option."
		exit 3
	fi
fi

echo "\tPip version 3+ found..."


#systemd is installed
if [ ! -d /lib/systemd/system/ ]
then
	if [ $SFLAG = 'f' ]
	then
		echo "You do not have systemd, if you wish to install anyway, run this script with the '-s' option"
		echo "NOTE: bot daemon will be placed in /var/www/slackbot/botd"
		exit 3
	fi
	SYSTEMD='f'
fi

echo "Done."



#Library installation
echo "installing python libraries..."

pip3 install pep3143daemon
pip3 install slacker

echo "Done."

echo "Installing Asymptote..."
echo "DEBUG:: $PKG"
if [ $PKG = 'apt' ]
then
	apt-get install asymptote
elif [ $PKG = 'pac' ]
then
	pacman -S asymptote
fi

echo "Done."

#creating user
echo "Creating slackbot user..."
useradd -M slackbot
echo "Done."


echo "Setting up files and directories..."
#Directory setup
mkdir -p /var/www/slackbot
mv commander.py /var/www/slackbot
mv core /var/www/slackbot/
mv modules /var/www/slackbot/
mv botd /var/www/slackbot/
if [ $SFLAG = 'f' ]
then
	mv slackbot.service /lib/systemd/system/
fi
touch /var/log/slackbot.log
touch /var/run/slackbot.pid
mkdir -p /etc/slackbot
echo $APIKEY > /etc/slackbot/API

#permissions setup
chown -R slackbot:slackbot /var/www/slackbot/
chown slackbot:slackbot /var/log/slackbot.log
chown slackbot:slackbot /var/run/slackbot.pid
chown -R slackbot:slackbot /etc/slackbot/

echo "Done."
