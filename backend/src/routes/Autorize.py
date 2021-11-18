from decouple import config
from flask_restful import Resource
from flask import redirect
import requests
import urllib.parse

class Autorize(Resource):
    def get(self):
        url = 'https://accounts.spotify.com/authorize?'
        scope = 'streaming user-read-playback-state user-read-currently-playing user-modify-playback-state user-read-private user-read-email'
        redirection = 'http://localhost:8989/callback/'
        autorization = f"{url}response_type=code&client_id={config('CLIENTID')}&redirect_uri={redirection}&scope={urllib.parse.quote(scope)}"

        return redirect(f'{autorization}')
