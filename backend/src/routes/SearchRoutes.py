from flask_restful import Resource
from flask import request
from src.search.Search import Search

class SearchSomething(Resource):
    def post(self):
        value = request.json['name']
        return Search().find(value)