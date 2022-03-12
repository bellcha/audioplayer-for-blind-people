import os
from text_to_speech import TTS

path = '/Users/bellcha/OneDrive'

class TTSFileBrowser:
    def __init__(self, path) -> None:
        self.path = path
        self.entries = os.listdir(self.path)
    
    def file_tree

dir_ = os.getcwd()

print(dir_)

parent = os.path.dirname(dir_)

print(parent)