#part 2


class SongNode:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title, artist, duration):
        new_song = SongNode(title, artist, duration)

        if self.head is None:
            self.head = self.tail = self.current = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song


#PART 4 ----------------------------------------------------------------------

import random


def shuffle_playlist(self):
    if not self.head:
        print("Playlist is empty")
        return

   # songs into a list
    songs = []
    temp = self.head
    while temp:
        songs.append(temp)
        temp = temp.next

    # Shuffle the list
    random.shuffle(songs)

    for i in range(len(songs)):
        if i > 0:
            songs[i].prev = songs[i-1]
        else:
            songs[i].prev = None

        if i < len(songs) - 1:
            songs[i].next = songs[i+1]
        else:
            songs[i].next = None

    # update
    self.head = songs[0]
    self.tail = songs[-1]
    self.current = self.head

    print("Playlist shuffled")

