from flask_restful import Resource
from src.TokenRetriever import TokenRetriever

class TokenGet(Resource):
    def get(self):
        return TokenRetriever().get()

class TokenRead(Resource):
    def get(self):
        return TokenRetriever().read();