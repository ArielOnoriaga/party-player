from decouple import config
from flask_restful import Resource
from flask import redirect
import urllib.parse

from src.Scopes import Scopes

class Autorize(Resource):
    def get(self):
        url = 'https://accounts.spotify.com/authorize?'
        scope = urllib.parse.quote(Scopes().get())
        redirection = 'http://localhost:8989/callback/'
        autorization = f"{url}response_type=code&client_id={config('CLIENTID')}&redirect_uri={redirection}&scope={scope}"

        return redirect(f'{autorization}')
