import json
import requests
import time
import os.path
from decouple import config

class TokenRetriever:
    def __init__(self):
        self.client = config('CLIENTID')
        self.secret = config('SECRET')
        self.url = "https://accounts.spotify.com/api/token"

    def getToken(self) -> list:
        response = requests.post(
            self.url,
            {
                'grant_type': 'client_credentials',
                'client_id': self.client,
                'client_secret': self.secret,
            }
        )
        responseArray = json.loads(
            json.dumps(
                response.json()
            )
        )
        return responseArray

    def saveToken(self, tokenData: list) -> None:
        currentUnixTime = int(time.time())
        tokenData.update({"created": currentUnixTime})

        tokenFile = 'token.txt'
        if os.path.exists(tokenFile) :
            with open(tokenFile, 'r+') as the_file:
                the_file.truncate(0)

        with open(tokenFile, 'a') as the_file:
            the_file.write(
                json.dumps(
                    tokenData
                )
            )
