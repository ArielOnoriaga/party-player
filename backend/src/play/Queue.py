import json
import os.path

class Queue:
    def __init__(self):
        self.queue = 'queue.txt';

    def createQueueIfNeeded(self) -> None:
        if not os.path.exists(self.queue) :
            open(self.queue, 'w+').close()

    def queueSong(self, uri: str, offset: int)-> None:
        Queue().createQueueIfNeeded()

        songData = {
            'uri': uri,
            'offset': offset
        }
        with open(self.queue, 'a') as queue:
            dataString = json.dumps(songData)
            queue.write(
                f'{dataString}\n'
            )
            queue.close()


    def getNextSong(self) -> list:
        with open(self.file, 'rw') as queue:
            songs = queue.readlines()
            nextSong = songs[1].strip()

            del songs[1]

            newQueue = open(self.queue, "w+")
            for line in lines:
                newQueue.write(line)

            newQueue.close()

