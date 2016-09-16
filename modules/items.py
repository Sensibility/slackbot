import json

itemsList = json.loads(open("/home/ocket8888/Downloads/items.json").read())

items = []
for item in itemsList['result']['items']:
	items.append("\""+item['localized_name']+"\"")


print(", ".join(items))