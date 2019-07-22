'''
Imports
'''
import requests, json, yaml, asyncio, websockets

class PBEndpoint:

	'''
	Statics
	'''
	ext = {

		"user"		:	"v2/users/me",
		"chats"		:	"v2/chats",
		"ephemeral"	:	"v2/ephemerals",
		"pushes"	:	"v2/pushes",
		"device"	:	"v2/devices",
		"all"		:	"v2/everything",
		"subs"		:	"v2/subscriptions",
		"channel"	:	"v2/channel-info",
		"upload"	:	"v2/upload-request"
	}

	api_url 		= 'https://api.pushbullet.com'

	websocket_url 	= 'wss://stream.pushbullet.com/websocket/'

	'''
	Ini
	'''
	def __init__(self, username):

		self.tokenheader 	= self.getToken(username)
		
		self.postheader 	= {

			'Access-Token'	: 	self.tokenheader['Access-Token'],
			'Content-Type'	: 	'application/json'
		}

	'''
	API Calls
	'''
	#get data
	def apiGET(self, extension):

		url 		= f'{self.api_url}/{self.ext[extension]}'
		response 	= requests.get(url, headers = self.tokenheader)

		return json.loads(response.text)
	
	#send it fam
	def apiPOST(self, extension, data = {}):
		
		url 		= f'{self.api_url}/{self.ext[extension]}'
		response 	= requests.post(url, headers = self.postheader, data = json.dumps(data))
		
		return json.loads(response.text)

	#delete
	def apiDELETE(self, extension, iden):
		
		url 		= f'{self.api_url}/{self.ext[extension]}/{iden}'		
		response 	= requests.delete(url, headers = header)

		return json.loads(response.text)
	
	'''
	Auth.
	'''
	def getToken(self, username):
		# OAuth for this later
		
		with open('access.yaml','r') as stream:

			accessdata = yaml.safe_load(stream)

		accessToken = accessdata[username]
		tokenheader = {'Access-Token':accessToken}

		return tokenheader

	'''
	Misc.
	'''
	def printJSON(self, jsondata):

		print(json.dumps(jsondata, indent = 2, ensure_ascii = False))



#ep = PBEndpoint("ciaran")

#ep.apiPOST('pushes',{'type':'note','title':'cunt','body':'ya shitcunt'})






