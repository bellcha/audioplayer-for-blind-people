from eyed3 import id3

tag = id3.Tag()

tag.parse("/Users/bellcha/Music/08_Colt_45.mp3")

print(tag.title)