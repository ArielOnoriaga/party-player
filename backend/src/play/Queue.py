import json
import os.path

from src.infraestructure.QueueDatabase import QueueDatabase


class Queue:
    def __init__(self):
        self.queue = QueueDatabase()

    def queueSong(self, uri: str, offset: int):
        self.queue.addSong(uri, offset)

        return {"success": True}

    def getNextSong(self, songId: int):
        return self.queue.getNextSong(songId)
