from decouple import config
from flask import redirect, Blueprint
from flask_restful import Resource
import urllib.parse

from src.Scopes import Scopes

autorization = Blueprint('autorization', __name__,)

@autorization.route('/autorize/')
def autorize(self):
    url = 'https://accounts.spotify.com/authorize?'
    scope = urllib.parse.quote(Scopes().get())
    redirection = 'http://localhost:8989/callback/'
    autorization = f"{url}response_type=code&client_id={config('CLIENTID')}&redirect_uri={redirection}&scope={scope}"

    return redirect(f'{autorization}')
