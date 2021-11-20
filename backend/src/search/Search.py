import urllib.parse
import requests
from src.TokenRetriever import TokenRetriever
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
        )

        return response.json()
