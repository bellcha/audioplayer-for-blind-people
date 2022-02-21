import os
from musicpd import (MPDClient, CommandError)

PATH = '/Users/bellcha/Music/'

class Album:
    def __init__(self, rel_path):
        self.rel_path = rel_path

    def name(self):
        return os.path.basename(self.rel_path)

client = MPDClient()
client.timeout = 60
client.idletimeout = None
client.user = 'bellcha'
client.connect()
os.system("mpc update")

mp3 = Album('/Users/bellcha/Music/08 Colt 45.mp3').name()

def play(path):
        mp3 = Album(path).name()
        try:
            print (f'playing {mp3}')
            client.add(mp3)
            client.play()
        except CommandError as e:
            print (e)


play(mp3)