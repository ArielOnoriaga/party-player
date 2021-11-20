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
        devices = Devices().get()
        firstDevice = devices[0]['id']
        #curl -X "PUT" "https://api.spotify.com/v1/me/player/play?device_id=a821c70236ad6919fea915982b819f907330ebfb" --data "{\"context_uri\":\"spotify:album:1bTgKomQYSkKYPD9UI9W4b\",\"offset\":{\"position\":0},\"position_ms\":0}" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQAPK0dpF26tbOxUfe_x_3vv8uNMlcwWtxjEfI2cUzwmMaA_QcVQx_sNLYsabuRFSUtAuuPiyA_X2Xj26YDrtASCbqXHWqR9iY147CVXiaUnXtvhL11k9A4VuomXfNquP9uJ4V76k4jkRhrCT_KjfryU6I9FjVC1OL0CMTMwWbShLNgkgPKaNIDhf1tHk7k"

        playUrl = f"https://api.spotify.com/v1/me/player/play?device_id={firstDevice}"
        uri = 'spotify:album:1bTgKomQYSkKYPD9UI9W4b';#imagine dragons enemy
        response = requests.put(
            playUrl,
            headers = self.headers,
            data = {
                "context_uri": uri,
                "offset": {
                    "position": 0
                },
                "position_ms": 0
            }
        )
        return response.json()