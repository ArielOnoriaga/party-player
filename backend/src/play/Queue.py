import json
import os.path

from src.infraestructure.QueueDatabase import QueueDatabase

class Queue:
    def __init__(self):
        self.queue = 'queue.txt';

    def createQueueIfNeeded(self) -> None:
        if not os.path.exists(self.queue) :
            open(self.queue, 'w+').close()

    def queueSong(self, uri: str, offset: int):
        QueueDatabase().addSong(uri, offset, 0)

        return {"success": True}

    def getNextSong(self, songId: int):
        return QueueDatabase().getNextSong(songId)