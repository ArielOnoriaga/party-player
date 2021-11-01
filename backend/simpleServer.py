from flask import Flask
from flask_restful import Resource, Api, reqparse
from src.TokenRetriever import TokenRetriever

app = Flask(__name__)
api = Api(app)

class Token(Resource):
    def get(self):
        return TokenRetriever().getToken()

api.add_resource(Token, '/token/')

parser = reqparse.RequestParser()

if __name__ == "__main__":
    app.run(
        debug=True,
        port=8080,
        host='0.0.0.0'
    )
