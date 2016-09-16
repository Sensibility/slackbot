#!/usr/bin/python3

import sys
import json



updates = json.loads(" ".join(sys.argv[1:]))

for update in updates['appnews']['newsitems']:
	if update['feedlabel'] == "Product Update":
		print(update['url'])
		break