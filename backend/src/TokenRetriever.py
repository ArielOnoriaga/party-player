from decouple import config
from src.Scopes import Scopes
from decouple import config
import json
import os.path
import base64
import requests
import time

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

        TokenRetriever().clearOldTokenData()

        TokenRetriever().saveTokenData(tokenData)

    def read(self) -> str:
        return TokenRetriever().getTokenData()['access_token']

    def getTokenData(self) -> list:
        tokenInfo = TokenRetriever().readTokenData()
        return TokenRetriever().updateIfNeeded(tokenInfo)

    def updateIfNeeded(self, tokenData: list) -> str:
        currentUnixTime = int(time.time())
        expiration = tokenData['created'] + tokenData['expires_in']

        if currentUnixTime - 100 > expiration:
            TokenRetriever().get()

        tokenInfo = TokenRetriever().readTokenData()
        return tokenInfo

    def refresh(self):
        tokenData = TokenRetriever().getTokenData()
        credentialsString = f'{self.client}:{self.secret}'
        credentialsBytes = credentialsString.encode("ascii")
        base64CredentialsBytes = base64.b64encode(credentialsBytes)
        base64CredentialsString = base64CredentialsBytes.decode("ascii")

        encodedCredentials = base64.b64encode(
            credentialsString.encode("ascii")
        );

        response = requests.post(
            self.url,
            headers = {
                'Authorization': f'Basic {base64CredentialsString}'
            },
            data = {
                'redirect_uri': self.url,
                'grant_type': 'refresh_token',
                'refresh_token': tokenData['refresh_token']
            },
            verify=True
        )
        responseJson = response.json()
        TokenRetriever().saveNewToken(responseJson)
        return True

    def saveNewToken(self, response) -> None:
        currentUnixTime = int(time.time())
        oldTokenData = TokenRetriever().readTokenData()

        response.update({
            "created": currentUnixTime,
            "refresh_token": oldTokenData['refresh_token']
        })

        TokenRetriever().clearOldTokenData()
        TokenRetriever().saveTokenData(response)

    def readTokenData(self) -> list:
        with open(self.file, 'r+') as file:
            return json.loads(file.read())

    def clearOldTokenData(self) -> None:
        if os.path.exists(self.file) :
            with open(self.file, 'r+') as file:
                file.truncate(0)

    def saveTokenData(self, tokenData) -> None:
        with open(self.file, 'a') as file:
            file.write(
                json.dumps(
                    tokenData
                )
            )
