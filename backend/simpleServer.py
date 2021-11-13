from flask import Flask
from flask_restful import Api, reqparse
from src.TokenRoutes import TokenGet, TokenRead

app = Flask(__name__)
api = Api(app)

api.add_resource(TokenGet, '/token/')
api.add_resource(TokenRead, '/token/read/')

parser = reqparse.RequestParser()

if __name__ == "__main__":
    app.run(
        debug=True,
        port=8080,
        host='0.0.0.0'
    )
