#part 2(janakesh)


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
#part 3(shrivatsaa)
# ---------------- NODE (Each Song) ----------------
class SongNode:
    def __init__(self, song):
        self.song = song      # song name
        self.next = None      # link to next song
        self.prev = None      # link to previous song


# --------------- MUSIC PLAYER ----------------
class MusicPlayer:
    def __init__(self):
        self.head = None      # first song
        self.current = None   # currently playing song

    # Add a song to playlist (Circular Doubly Linked List)
    def add_song(self, song):
        new_song = SongNode(song)

        # If playlist empty → first song
        if self.head is None:
            self.head = new_song
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
            return

        # Insert at end
        last = self.head.prev

        last.next = new_song
        new_song.prev = last

        new_song.next = self.head
        self.head.prev = new_song

    # PLAY current song
    def play(self):
        if self.current is None:
            print("Playlist is empty")
        else:
            print("Now Playing:", self.current.song)

    # NEXT song (O(1))
    def next_song(self):
        if self.current is None:
            print("No songs in playlist")
        else:
            self.current = self.current.next
            print("Next Song:", self.current.song)

    # PREVIOUS song (O(1))
    def previous_song(self):
        if self.current is None:
            print("No songs in playlist")
        else:
            self.current = self.current.prev
            print("Previous Song:", self.current.song)

    # Display playlist
    def show_playlist(self):
        if self.head is None:
            print("Playlist empty")
            return

        temp = self.head
        print("\nPlaylist:")
        while True:
            print(temp.song)
            temp = temp.next
            if temp == self.head:
                break


# ---------------- MENU (USER INPUT) ----------------
player = MusicPlayer()

while True:
    print("\n------ MUSIC PLAYER ------")
    print("1. Add Song")
    print("2. Play Current Song")
    print("3. Next Song")
    print("4. Previous Song")
    print("5. Show Playlist")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter song name: ")
        player.add_song(name)

    elif choice == 2:
        player.play()

    elif choice == 3:
        player.next_song()

    elif choice == 4:
        player.previous_song()

    elif choice == 5:
        player.show_playlist()

    elif choice == 6:
        print("Exiting Music Player...")
        break

    else:
        print("Invalid choice")

#part 4(yeswanth)

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

