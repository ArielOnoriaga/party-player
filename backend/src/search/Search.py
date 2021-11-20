import urllib.parse
import requests

from src.responses.Song import Song
from src.Headers import Headers

class Search:
    def __init__(self):
        self.url = "https://api.spotify.com/v1/search"

    def find(self, search: str):
        search = urllib.parse.quote(search)
        searchUrl = f'{self.url}?q={search}&type=album,artist,track&limit=30'

        response = requests.get(
            searchUrl,
            headers = Headers().get()
        ).json()

        response['tracks'] = list(
            map(Song().create,response['tracks']['items'])
        )

        return response
