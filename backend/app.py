from flask import Flask
from flask_restful import Api, reqparse
from flask_cors import CORS
from flask_socketio import SocketIO

from src.routes.Autorize import autorization
from src.routes.Player import player

from src.routes.SearchRoutes import SearchSomething
from src.routes.TokenRoutes import TokenGet, TokenRead, TokenRefresh
app = Flask(__name__)

socketio = SocketIO(app)

app.config.update(
    host = '0.0.0.0',
    port = 8080,
    debug=True,
)

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
    allow_headers=['Content-Type', 'Access-Control-Allow-Origin'],
    upport_credentials=True
)

app.register_blueprint(autorization)
app.register_blueprint(player, url_prefix='/player')

api.add_resource(SearchSomething, '/search/')
api.add_resource(TokenGet, '/callback/')
api.add_resource(TokenRead, '/token/read/')
api.add_resource(TokenRefresh, '/token/refresh/')

api.add_resource(GetDevices, '/player/devices')
api.add_resource(SetVolume, '/player/volume')

parser = reqparse.RequestParser()

if __name__ == "__main__":
    socketio.run(
        app,
        port=8080,
        host='0.0.0.0'
    )
