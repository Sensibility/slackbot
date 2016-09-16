#!/usr/bin/python3

import sys
import json

patch=json.loads(" ".join(sys.argv[1:]))['patchNotes'][0]
output=patch['patchVersion']
rawhtml=patch['detail']
print("Version "+output+"\n"+rawhtml)