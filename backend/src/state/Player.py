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
            headers=self.headers
        )

        return response.json()

    def play(self, uri, offset):
        requestData = {
            "context_uri": uri,
            "offset": {
                "position": offset
            },
            "position_ms": 0
        }

        Player().playRequest(requestData)

        return {"success": True}

    def pause(self):
        device = self.currentDevice()

        if device == '':
            device = Devices().getDefault()['id']

        playUrl = f"{self.endpoint}/pause?device_id={device}"

        requests.put(
            playUrl,
            headers=self.headers,
        )

        return {"success": True}

    def resume(self):
        Player().playRequest({})
        return {"success": True}

    def playRequest(self, requestData) -> None:
        device = self.currentDevice()

        if device == '':
            device = Devices().getDefault()['id']

        playUrl = f"{self.endpoint}/play?device_id={device}"

        requests.put(
            playUrl,
            headers=self.headers,
            data=json.dumps(requestData)
        )

    def volume(self, volume: int):
        firstDevice = Devices().getDefault()['id']

        volumeParameter = f'volume_percent={volume}'
        deviceParameter = f'device_id={firstDevice}'

        playUrl = f"{self.endpoint}/volume?{volumeParameter}&{deviceParameter}"

        requests.put(
            playUrl,
            headers=self.headers,
        )

        return {"success": True}

    def currentDevice(self):
        currentState = self.state()
        return currentState['device']['id'] or ''
