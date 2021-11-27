import json
from pydblite import Base
import os.path

class QueueDatabase:
    def __init__(self):
        self.file = './src/infraestructure/party.pdl'

    def setUpDatabase(self) -> None:
        if not os.path.exists(self.file) :
            db = Base(self.file)
            db.create('uri', 'offset', 'time')
            db.create_index('uri', 'offset')

    def getDatabase(self):
        QueueDatabase().setUpDatabase()
        return Base(self.file)

    def addSong(self, albumUri: str, songOffset: int, miliseconds: int):
        db = QueueDatabase().getDatabase()

        db.open()
        db.insert(uri=albumUri, offset=songOffset, time=miliseconds)
        db.commit()

        return {"success": True}

    def getNextSong(self, currentId: int):
        db = QueueDatabase().getDatabase()

        db.open()
        quantity = len(db)
        nextId = currentId+1
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
