import json
import urllib.parse
import requests
from src.TokenRetriever import TokenRetriever


class Devices:
    def __init__(self):
        self.token = TokenRetriever().read()
        self.url = "https://api.spotify.com/v1/me/player/devices"

    def get(self):
        requestHeaders = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
        }
        response = requests.get(
            self.url,
            headers=requestHeaders,
        )
        return response.json()

    def getDefault(self):
        return Devices().get()['devices'][0]
