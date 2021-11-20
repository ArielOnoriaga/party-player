import json
import urllib.parse
import requests
from src.TokenRetriever import TokenRetriever
from src.play.Devices import Devices

class Player:
    def __init__(self):
        self.token = TokenRetriever().read()
        self.endpoint = 'https://api.spotify.com/v1/me/player'
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

    def play(self, uri: str):
        firstDevice = Devices().getDefault()['id']

        playUrl = f"https://api.spotify.com/v1/me/player/play?device_id={firstDevice}"
        requestData = {"context_uri": uri,"offset": {"position": 0},"position_ms": 0}
        response = requests.put(
            playUrl,
            headers = self.headers,
            data = json.dumps(requestData)
        )
        return True

    def pause(self):
        firstDevice = Devices().getDefault()['id']

        playUrl = f"https://api.spotify.com/v1/me/player/pause?device_id={firstDevice}"
        response = requests.put(
            playUrl,
            headers = self.headers,
        )
        return True