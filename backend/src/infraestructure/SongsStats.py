import json
from pydblite import Base
import os.path

class SongsStats:
    def __init__(self):
        self.file = './src/infraestructure/stats.pdl'

    def setUpDatabase(self) -> None:
        if not os.path.exists(self.file) :
            db = Base(self.file)
            db.create('uri', 'offset', 'likes', 'dislikes')
            db.create_index('uri', 'offset', 'likes', 'dislikes')

    def getDatabase():
        SongsStats().setUpDatabase()
        return Base(SongsStats().file)

    def addSong(albumUri: str, songOffset: int):
        db = SongsStats.getDatabase()

        db.open()
        record = db(uri=albumUri, offset=songOffset)
        if not record :
            db.insert(
                albumUri,
                songOffset,
                0,
                0
            )
            db.commit()
            record = db(uri=albumUri, offset=songOffset)

        return {
            "id": record[0]['__id__']
        }

    def likeSong(albumUri: str, songOffset: int):
        db = SongsStats.getDatabase()
        db.open()
        exists = db(uri=albumUri, offset=songOffset)
        if exists:
            db.update(
                exists[0],
                likes=exists[0]['likes']+1
            )
            db.commit()
            return {"success": True}
        return {
            "error": "song is not registered"
        }

    def dislikeSong(albumUri: str, songOffset: int):
        db = SongsStats.getDatabase()
        db.open()
        exists = db(uri=albumUri, offset=songOffset)
        if exists:
            db.update(
                exists[0],
                dislikes=exists[0]['dislikes']+1
            )
            db.commit()
            return {"success": True}
        return {
            "error": "song is not registered"
        }

    def songIsBanned(albumUri: str, songOffset: int) -> bool:
        db = SongsStats.getDatabase()
        db.open()
        exists = db(uri=albumUri, offset=songOffset)
        if exists:
            songLikes = exists[0]['likes']
            songDislikes = exists[0]['dislikes']
            threshold = 0.85
            return (songDislikes/(songLikes+songDislikes)) >= threshold

        return False

    def showSongs() -> None:
        db = SongsStats.getDatabase()

        db.open()
        for register in db:
            print(register)
