from flask_restful import Resource
from flask import request, Blueprint
from src.state.Player import Player
from src.play.Devices import Devices
from src.play.Queue import Queue

player = Blueprint('player', __name__,)

@player.route('/state/')
def state():
    return Player().state()

@player.route('/play/')
def play():
    albumUri = request.json['albumUri']
    offset = request.json['offset']

    return Player().play(albumUri, offset)

@player.route('/pause/')
def pause():
    return Player().pause()

@player.route('/resume/')
def resume():
    return Player().resume()

@player.route('/devices/')
def devices():
    return Devices().get()

@player.route('/volume')
def volume():
    volume = request.json['volume']
    return Player().volume(volume)

@player.route('/queue')
def queue():
    uri = request.json['albumUri']
    offset = request.json['offset']
    return Queue().queueSong(uri, offset)
