from flask_restful import Resource
from src.state.Player import Player
from src.play.Devices import Devices

class PlayerState(Resource):
    def get(self):
        return Player().state()

class PlaySomething(Resource):
    def get(self, uri: str):
        return Player().play(uri)

class Pause(Resource):
    def get(self):
        return Player().pause()

class Resume(Resource):
    def get(self):
        return Player().resume()

class GetDevices(Resource):
    def get(self):
        return Devices().get()
