import json
import os.path

from pydblite import Base


class SongsStats:
    def __init__(self, filename=None):
        basePath = "./src/infraestructure"
        dbFile = filename or 'stats'
        self.file = f'{basePath}/{dbFile}.pdl'

    def setUpDatabase(self) -> None:
        if not os.path.exists(self.file):
            db = Base(self.file)
            db.create('uri', 'offset', 'likes', 'dislikes')
            db.create_index('uri', 'offset', 'likes', 'dislikes')

    def getDatabase(self) -> Base:
        self.setUpDatabase()
        return Base(self.file)

    def addSong(self, albumUri: str, songOffset: int) -> object:
        db = self.getDatabase()

        db.open()
        record = db(uri=albumUri, offset=songOffset)
        if not record:
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

    def likeSong(self, albumUri: str, songOffset: int):
        db = self.getDatabase()
        db.open()
        exists = db(uri=albumUri, offset=songOffset)
        if exists:
            db.update(
                exists[0],
                likes=exists[0]['likes'] + 1
            )
            db.commit()
            return {"success": True}
        return {
            "error": "song is not registered"
        }

    def dislikeSong(self, albumUri: str, songOffset: int):
        db = self.getDatabase()
        db.open()
        exists = db(uri=albumUri, offset=songOffset)
        if exists:
            db.update(
                exists[0],
                dislikes=exists[0]['dislikes'] + 1
            )
            db.commit()
            return {"success": True}
        return {
            "error": "song is not registered"
        }

    def songIsBanned(self, albumUri: str, songOffset: int) -> bool:
        db = self.getDatabase()
        db.open()
        exists = db(uri=albumUri, offset=songOffset)
        if exists:
            songLikes = exists[0]['likes']
            songDislikes = exists[0]['dislikes']
            threshold = 0.85

            totalVotes = songLikes + songDislikes
            if totalVotes == 0:
                return False

            hasMinimumValidations = totalVotes > 10
            hasFewerLikes = (songDislikes / (totalVotes)) >= threshold
            return hasMinimumValidations and hasFewerLikes

        return False

    def showSongs(self) -> None:
        db = self.getDatabase()

        db.open()
        for register in db:
            print(register)
