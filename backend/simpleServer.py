from flask import Flask
from flask_restful import Api, reqparse

from src.routes.Autorize import Autorize
from src.routes.PlayerRoutes import PlayerRoutes
from src.routes.SearchRoutes import SearchSomething
from src.routes.TokenRoutes import TokenGet, TokenRead

app = Flask(__name__)
api = Api(app)

api.add_resource(Autorize, '/autorize/')
api.add_resource(PlayerRoutes, '/state/')
api.add_resource(SearchSomething, '/search/<songOrArtist>')
api.add_resource(TokenGet, '/callback/')
api.add_resource(TokenRead, '/token/read/')

parser = reqparse.RequestParser()

if __name__ == "__main__":
    app.run(
        debug=True,
        port=8080,
        host='0.0.0.0'
    )
