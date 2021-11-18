from flask_restful import Resource
from flask import request
from src.TokenRetriever import TokenRetriever

class TokenGet(Resource):
    def get(self):
        code = request.args.get('code')
        return TokenRetriever().get(code)

class TokenRead(Resource):
    def get(self):
        return TokenRetriever().read();
