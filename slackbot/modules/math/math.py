"""
Contains a function to generate and upload a LaTeX-rendered math image.
"""
import subprocess
import sys
import typing

def uploadLatex(math: typing.List[str], slackAPI: object, channel: object, users: list) -> str:
	"""
	Generates a LaTeX math image from the LaTeX source contained in `math`, and posts it to the
	api `slackapi` in channel `channel`.

	Returns a string describing any errors that occurred.
	"""
	toParse = "".join(math).replace("&amp;","&")

	# create a temporary directory
	response = subprocess.run(["mktemp", "-d"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# check for errors
	if response.returncode != 0 or response.stderr.decode() != '':
		return "EE: latex: couldn't make temp. dir: '"+response.stderr.decode()+"'"

	# Decode and store the temporary directory name
	latexdir = response.stdout.decode().splitlines()[0]

	# Generate the image using l2p
	response = subprocess.run(["l2p", "-i", toParse, "-o", latexdir+"/latex_output.png"],
	                          stdout=subprocess.PIPE,
	                          stderr=subprocess.PIPE)

	# Check for errors, both posting to the channel (because it's probable that a user messed up)
	# as well as logging to the logfile
	if response.stderr.decode() != '':
		msg = "Unable to parse expression: %s: %s"
		slackAPI.chat.post_message(channel['name'],
		                           msg % ("`%s` because" % toParse, "`%s`" % response.stderr.decode()))
		return "EE: latex: " + msg % ("'%s'" % toParse, "'%s'" % response.stderr.decode())

	# If all went well, upload then delete the file
	slackAPI.files.upload(latexdir+"/latex_output.png", channels=channel['id'])
	retstr = "II: latex: uploaded image to slack (input: '%s')" % toParse
	response = subprocess.run(["rm", "-r", "-f", latexdir], stderr=subprocess.PIPE)
	if response.returncode != 0 or response.stderr.decode() != "":
		return retstr+"\nEE: latex: error encountered during cleanup: '%s'" % response.stderr.decode()
	return retstr
