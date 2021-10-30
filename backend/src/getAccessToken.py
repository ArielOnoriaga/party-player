import json
import requests
import time
import os.path
from decouple import config

client = config('CLIENTID')
secret = config('SECRET')

url = "https://accounts.spotify.com/api/token"

response = requests.post(
    url,
    {
        'grant_type': 'client_credentials',
        'client_id': client,
        'client_secret': secret,
    }
)
jsonResponse = response.json()
responseArray = json.loads(json.dumps(jsonResponse))
currentUnixTime = int(time.time())
responseArray.update({"created": currentUnixTime})

token = responseArray['access_token']
expiration = responseArray['expires_in']

tokenFile = 'token.txt'
if os.path.exists(tokenFile) :
    with open(tokenFile, 'r+') as the_file:
        the_file.truncate(0)

with open(tokenFile, 'a') as the_file:
    the_file.write(json.dumps(responseArray))
