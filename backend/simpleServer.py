from flask import Flask
from flask_restful import Api, reqparse
from flask_cors import CORS

from src.routes.Autorize import Autorize
from src.routes.SearchRoutes import SearchSomething

from src.routes.TokenRoutes import TokenGet, TokenRead
from src.routes.PlayerRoutes import PlaySomething, GetDevices, PlayerState

app = Flask(__name__)

api = Api(app)

CORS(
    app,
    resources = {
        r"/search/": {
            "origins": "*"
        },
        r"/player/*": {
            "origins": "*"
        },
    },
    origins='localhost:8990',
    allow_headers=['Content-Type', 'Access-Control-Allow-Origin'],
    upport_credentials=True
)

api.add_resource(Autorize, '/autorize/')
api.add_resource(SearchSomething, '/search/')
api.add_resource(TokenGet, '/callback/')
api.add_resource(TokenRead, '/token/read/')

api.add_resource(PlayerState, '/player/state/')
api.add_resource(PlaySomething, '/player/play/<uri>')
api.add_resource(GetDevices, '/player/devices')

parser = reqparse.RequestParser()

if __name__ == "__main__":
    app.run(
        debug=True,
        port=8080,
        host='0.0.0.0'
    )
