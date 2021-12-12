import json
from pydblite import Base
import os.path


class QueueDatabase:
    def __init__(self, filename=None):
        dbFile = filename or "queue"
        basePath = "./src/infraestructure"
        self.file = f'{basePath}/{dbFile}.pdl'

    def setUpDatabase(self) -> None:
        if not os.path.exists(self.file):
            db = Base(self.file)
            db.create('uri', 'offset', 'time')
            db.create_index('uri', 'offset')

    def getDatabase(self) -> Base:
        return Base(self.file)

    def addSong(self, albumUri: str, songOffset: int, miliseconds: int):
        db = self.getDatabase()

        db.open()
        db.insert(albumUri, songOffset, miliseconds)
        db.commit()

        return {"success": True}

    def removeSong(self, albumUri: str, songOffset: int):
        db = self.getDatabase()

        db.open()
        for song in (db(uri=albumUri, offset=songOffset)):
            db.delete(song)
            db.commit()
            return {"success": True}
        return {"success": True}

    def getNextSong(self, currentId: int):
        db = self.getDatabase()

        db.open()
        quantity = len(db)
        nextId = currentId + 1
        if (nextId >= quantity):
            return {
                "error": "there is no next song"
            }

        nextItem = db[nextId]
        return {
            "id": nextItem['__id__'],
            "albumUri": nextItem['uri'],
            "offset": nextItem['offset'],
        }

    def showSongs(self) -> None:
        db = self.getDatabase()

        db.open()
        for register in db:
            print(register)
