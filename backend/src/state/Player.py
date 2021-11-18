import json
import requests
from src.TokenRetriever import TokenRetriever

class Player:
    def __init__(self):
        self.token = TokenRetriever().read()
        self.endpoint = 'https://api.spotify.com/v1/me/playlists'
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def state(self):
        response = requests.get(
            self.endpoint,
            headers = self.headers
        )

        return response.json()
