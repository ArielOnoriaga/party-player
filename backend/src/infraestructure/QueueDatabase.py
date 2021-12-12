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

    def addSong(self, albumUri: str, songOffset: int):
        db = self.getDatabase()

        db.open()
        db.insert(albumUri, songOffset, 0)
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
        try:
            for record in db:
                if record['__id__'] > currentId:
                    return {
                        "id": record['__id__'],
                        "albumUri": record['uri'],
                        "offset": record['offset'],
                    }
            return {
                "error": "there is no next song"
            }
        except:
            return {
                "error": "there is no next song"
            }

    def showSongs(self) -> None:
        db = self.getDatabase()

        db.open()
        for register in db:
            print(register)
