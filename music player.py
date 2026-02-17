import pygame
import os
import random

# initialize audio system
pygame.mixer.init()
SONG_FOLDER = "songs"

class SongNode:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class MusicPlayer:
    def __init__(self):
        self.head = None
        self.current = None

    
    def add_song(self, song):
        new_song = SongNode(song)

      
        if self.head is None:
            self.head = new_song
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
            print(song, "added as first song.")
            return

        last = self.head.prev

        last.next = new_song
        new_song.prev = last
        new_song.next = self.head
        self.head.prev = new_song

        print(song, "added to playlist.")

    
    def play(self):
        if self.current is None:
            print("Playlist empty!")
            return

        song_path = os.path.join(SONG_FOLDER, self.current.song)

        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            print("▶ Now Playing:", self.current.song)
        except:
            print("MP3 file not found inside songs folder!")

    
    def next_song(self):
        if self.current is None:
            print("No songs available.")
            return

        self.current = self.current.next
        self.play()


    def previous_song(self):
        if self.current is None:
            print("No songs available.")
            return

        self.current = self.current.prev
        self.play()

    def pause(self):
        pygame.mixer.music.pause()
        print("⏸ Paused")
    def resume(self):
        pygame.mixer.music.unpause()
        print("▶ Resumed")

    def stop(self):
        pygame.mixer.music.stop()
        print("⏹ Stopped")

    def shuffle_song(self):
        if self.head is None:
            print("Playlist empty.")
            return

        temp = self.head
        count = 1
        while temp.next != self.head:
            temp = temp.next
            count += 1

        pos = random.randint(1, count)
        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next

        self.current = temp
        print("🔀 Shuffle Playing:", self.current.song)
        self.play()

    def show_playlist(self):
        if self.head is None:
            print("Playlist empty.")
            return

        print("\n🎶 Playlist:")
        temp = self.head
        i = 1

        while True:
            marker = ""
            if temp == self.current:
                marker = "  <-- playing"

            print(str(i) + ".", temp.song + marker)

            temp = temp.next
            i += 1
            if temp == self.head:
                break


# ---------- MENU ----------
player = MusicPlayer()

while True:
    print("\n========== MUSIC PLAYER ==========")
    print("1. Add Song")
    print("2. Play")
    print("3. Next")
    print("4. Previous")
    print("5. Pause")
    print("6. Resume")
    print("7. Shuffle")
    print("8. Show Playlist")
    print("9. Stop")
    print("10. Exit")

    try:
        choice = int(input("Enter choice: "))
    except:
        print("Enter numbers only!")
        continue

    if choice == 1:
        name = input("Enter song filename (example: believer.mp3): ")
        player.add_song(name)

    elif choice == 2:
        player.play()

    elif choice == 3:
        player.next_song()

    elif choice == 4:
        player.previous_song()

    elif choice == 5:
        player.pause()

    elif choice == 6:
        player.resume()

    elif choice == 7:
        player.shuffle_song()

    elif choice == 8:
        player.show_playlist()

    elif choice == 9:
        player.stop()

    elif choice == 10:
        player.stop()
        print("Goodbye 🎧")
        break

    else:
        print("Invalid choice!")

