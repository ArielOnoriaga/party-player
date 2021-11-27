from flask_restful import Resource
from flask import request, Blueprint
from src.state.Player import Player
from src.play.Devices import Devices
from src.play.Queue import Queue

player = Blueprint('player', __name__,)

@player.route('/state/', methods = ['GET'])
def state():
    return Player().state()

@player.route('/play/', methods = ['POST'])
def play():
    albumUri = request.json['albumUri']
    offset = request.json['offset']

    return Player().play(albumUri, offset)

@player.route('/pause/', methods = ['GET'])
def pause():
    return Player().pause()

@player.route('/resume/', methods = ['GET'])
def resume():
    return Player().resume()

@player.route('/devices/', methods = ['GET'])
def devices():
    return Devices().get()

@player.route('/volume', methods = ['POST'])
def volume():
    volume = request.json['volume']
    return Player().volume(volume)

@player.route('/queue/', methods = ['POST'])
def queue():
    uri = request.json['albumUri']
    offset = request.json['offset']
    return Queue().queueSong(uri, offset)

@player.route('/next/', methods = ['POST'])
def nextSong():
    currentId = request.json['id']
    return Queue().getNextSong(currentId)
