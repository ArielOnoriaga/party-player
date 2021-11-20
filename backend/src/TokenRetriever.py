from decouple import config
import json
import os.path
import requests
import time

from src.Scopes import Scopes

class TokenRetriever:
    def __init__(self):
        self.client = config('CLIENTID')
        self.secret = config('SECRET')
        self.url = "https://accounts.spotify.com/api/token"
        self.file = 'token.txt';

    def get(self, code: str) -> list:
        response = requests.post(
            self.url,
            data = {
                'redirect_uri': 'http://localhost:8989/callback/',
                'grant_type': 'authorization_code',
                'scope': Scopes().get(),
                'client_id': self.client,
                'client_secret': self.secret,
                'code': str(code)
            },
            verify=True
        )

        result = response.json()
        TokenRetriever().save(result)

        return result

    def save(self, tokenData: list) -> None:
        currentUnixTime = int(time.time())
        tokenData.update({"created": currentUnixTime})

        if os.path.exists(self.file) :
            with open(self.file, 'r+') as file:
                file.truncate(0)

        with open(self.file, 'a') as file:
            file.write(
                json.dumps(
                    tokenData
                )
            )

    def read(self) -> str:
        with open(self.file, 'r+') as file:
            tokenInfo = json.loads(file.read())
            return TokenRetriever().updateIfNeeded(tokenInfo)

    def updateIfNeeded(self, tokenData: list) -> str:
        currentUnixTime = int(time.time())
        expiration = tokenData['created'] + tokenData['expires_in']

        if currentUnixTime - 100 > expiration:
            TokenRetriever().save(TokenRetriever().get())

        with open(self.file, 'r+') as file:
            tokenInfo = json.loads(file.read())
            return tokenInfo['access_token']
