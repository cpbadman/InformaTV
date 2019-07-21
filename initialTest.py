import requests
import json
import yaml

#accessdata = None

username = 'ciaran'

#OAuth for this later
with open('access.yaml','r') as stream:
	accessdata = yaml.safe_load(stream)
accessToken = accessdata[username]
tokenHeader = {'Access-Token':accessToken}

r = requests.get('https://api.pushbullet.com/v2/users/me',headers = tokenHeader)

print(json.dumps(json.loads(r.text), indent = 4, ensure_ascii = False))

