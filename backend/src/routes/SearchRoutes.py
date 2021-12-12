from flask import request

from flask_restful import Resource

from src.search.Search import Search


class SearchSomething(Resource):
    def post(self):
        value = request.json['name']
        return Search().find(value)
