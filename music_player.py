import os
from musicpd import (MPDClient, CommandError)


class MusicPlayer:
    def __init__(self, file):
       self.client = MPDClient()
       self.file = file 

    def play(self, path):
        self.client.clear()
        try:
            print (f'playing {path}')
            self.client.add(path[len(PATH) + 1:])
            self.client.client.play()
        except CommandError as e:
            print (e)

    def maybe_set_bookmark(self):
        elapsed = int(float(self.client.status().get('elapsed', "0")))
        index = self.file.parent.entries().index(self.file)
        if elapsed > 30:
            print (f'creating bookmark at {index}-{elapsed}')
            with open(self.file.parent.meta_file('bookmark.txt'), 'w') as f:
                f.write(str(index) + '\n')
                f.write(str(elapsed) + '\n')
        else:
            print (f'not creating bookmark, elapsed = {elapsed} <= 30s')

    def handle_up(self):
        self.maybe_set_bookmark()
        return super(MusicPlayer, self).handle_up()

    def handle_pos1(self):
        self.maybe_set_bookmark()
        return super(MusicPlayer, self).handle_pos1()

    def handle_play_pause(self):
        os.system('mpc toggle')

    def handle_stopped(self):
        return self.file.parent.next_entry(self.file)

    def handle_right(self):
        os.system('mpc seek +00:01:00')

    def handle_left(self):
        os.system('mpc seek -00:01:00')

    def handle_tick(self):
        if self.client.status()['state'] == 'stop':
            return self.handle_stopped()

    def handle_bookmark(self):
        return get_screen_for_bookmark(self.file.parent)