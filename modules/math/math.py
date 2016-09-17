#!/usr/bin/python3
import subprocess
import sys

def uploadLatex(math, slackAPI, channel, users):
	toParse="".join(math).replace("&amp;","&")
	response=subprocess.run(["mktemp", "-d"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	if response.returncode!=0 or response.stderr.decode() != '':
		return "EE: latex: couldn't make temp. dir: '"+response.stderr.decode()+"'"
	latexdir=response.stdout.decode().splitlines()[0]
	response=subprocess.run(["l2p", "-i", toParse, "-o", latexdir+"/latex_output.png"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	if response.stderr.decode() != '':
		slackAPI.chat.post_message(channel['name'], "Unable to parse expression: `"+math+"` because: `"+response.stderr.decode()+"`")
		return "EE: latex: unable to compile '"+toParse+"' :"+response.stderr.decode()
	slackAPI.files.upload(latexdir+"/latex_output.png", channels=channel['id'])
	retstr = "II: latex: uploaded image to slack (input: "+toParse+")"
	response=subprocess.run(["rm", "-r", "-f", latexdir], stderr=subprocess.PIPE)
	if response.returncode != 0 or response.stderr.decode() != "":
		return retstr+"\nEE: latex: error encountered during cleanup"
	return retstr