import json
import os.path

class Queue:
    def __init__(self):
        self.queue = 'queue.txt';

    def createQueueIfNeeded(self) -> None:
        if not os.path.exists(self.queue) :
            open(self.queue, 'w+').close()

    def queueSong(self, uri: str, offset: int):
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

        return {"success": True}


    def getNextSong(self):
        with open(self.queue, 'r+') as file:
            lines = file.readlines()
            file.close()

            nextSong = lines[0]

            del lines[0]

            new_file = open(self.queue, "w+")

            for line in lines:
                cleanLine = line.strip("\n");
                new_file.write(
                    f'{line}\n'
                )
            new_file.close()

            return json.dumps(json.loads(nextSong))

