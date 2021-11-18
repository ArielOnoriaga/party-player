from flask_restful import Resource
from src.state.Player import Player

class PlayerRoutes(Resource):
    def get(self):
        return Player().state()
