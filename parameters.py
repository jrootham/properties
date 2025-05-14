import json

def get(name):
	with open(name, "r") as file: 
		text = file.read()
	return json.loads(text)

