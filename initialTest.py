import requests
import json

#OAuth for this later
accessToken = 'o.SJYfTHRtgStE2nYhmTkJET5uCrx6vm0h'
tokenHeader = {'Access-Token':accessToken}


r = requests.get('https://api.pushbullet.com/v2/users/me',headers = None)

print(json.dumps(json.loads(r.text), indent = 4, ensure_ascii = False))

