import json
import urllib.parse
import requests
from src.TokenRetriever import TokenRetriever

class Search:
    def __init__(self):
        self.token = TokenRetriever().read();
        self.url = "https://api.spotify.com/v1/search"

    def find(self, songOrArtist: str):
        searchUrl = f'{self.url}?q={urllib.parse.quote(songOrArtist)}&type=album,artist,track&limit=30'

        response = requests.get(
            searchUrl,
            headers = {
                'Authorization': f'Bearer {self.token}',
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        )
        return response.json()
