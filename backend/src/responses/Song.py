import json

class Song:
  def create(self, response):
    return {
      "name": response['name'],
      "preview": response['preview_url'],
      "uri": response['uri'],
      "offset": response['track_number'] - 1,
      "albumUri": response['album']['uri']
    }