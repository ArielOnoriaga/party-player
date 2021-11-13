from flask_restful import Resource
from src.search.Search import Search

class SearchSomething(Resource):
    def get(self, songOrArtist: str):
        return Search().find(songOrArtist)