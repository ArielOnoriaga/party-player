import json
from pydblite import Base
import os.path

class QueueDatabase:
    def __init__(self):
        self.file = './src/infraestructure/queue.pdl'

    def setUpDatabase(self) -> None:
        if not os.path.exists(self.file) :
            db = Base(self.file)
            db.create('uri', 'offset', 'time')
            db.create_index('uri', 'offset')

    def getDatabase():
        instance = QueueDatabase()
        instance.setUpDatabase()
        return Base(instance.file)

    def addSong(albumUri: str, songOffset: int, miliseconds: int):
        db = QueueDatabase.getDatabase()

        db.open()
        db.insert(albumUri, songOffset, miliseconds)
        db.commit()

        return {"success": True}

    def getNextSong(currentId: int):
        db = QueueDatabase.getDatabase()

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

    def showSongs() -> None:
        db = QueueDatabase.getDatabase()

        db.open()
        for register in db:
            print(register)