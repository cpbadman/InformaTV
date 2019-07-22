import requests
import json
import yaml


def getToken(username):
	#OAuth for this later
	with open('access.yaml','r') as stream:
		accessdata = yaml.safe_load(stream)
	accessToken = accessdata[username]
	tokenHeader = {'Access-Token':accessToken}

	return tokenHeader

def printJSON(jsondata):

	print(json.dumps(jsondata, indent = 2, ensure_ascii = False))

def apiRequest(api_url, args, header):

	url = f'{api_url}/{args}'
	response = requests.get(url, headers = header)
	return json.loads(response.text)

def apiPost(api_url, args, header, data = {}):
	
	url = f'{api_url}/{args}'
	response = requests.post(url, data = json.dumps(data), headers = header)
	printJSON(data)
	return json.loads(response.text)

def execute():

	api_url = 'https://api.pushbullet.com'

	accessheader = getToken('ciaran')

	chrm = apiRequest(api_url,'v2/devices', accessheader)['devices'][0]['iden']

	postheader = {
		'Content-Type': 'application/json',
		'Access-Token':accessheader['Access-Token']
	}

	examplePush = {
		'type':'note',
		'title':'test',
		'body':'this is an initial test',
	}

	#

	p = apiPost(api_url, f'v2/pushes', postheader, data = examplePush)
	printJSON(p)

execute()
#printJSON(devices)
