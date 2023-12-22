import csv

def load_songs():
    try:
        with open("songs.csv", "r") as file:
            reader = csv.reader(file)
            songs = list(reader)
        return songs
    except FileNotFoundError:
        return []

def save_songs(songs):
    with open("songs.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(songs)

def display_songs(songs):
    print("Song List")
    print(f"{len(songs)} songs loaded.")
    print("Menu:")
    print("D - Display songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")

def add_song(songs):
    title = input("Title: ")
    while not title.strip():
        print("Input can not be blank.")
        title = input("Title: ")

    artist = input("Artist: ")
    while not artist.strip():
        print("Input can not be blank.")
        artist = input("Artist: ")

    year = input("Year: ")
    while not year.isdigit() or int(year) <= 0:
        print("Invalid input; enter a valid number.")
        year = input("Year: ")

    songs.append([title, artist, year, "u"])
    print(f"{title} by {artist} ({year}) added to song list.")

def complete_song(songs):
    display_songs_status(songs)
    try:
        song_number = int(input("Enter the number of a song to mark as learned.\n>>> "))
        if 1 <= song_number <= len(songs):
            if songs[song_number - 1][3] == "l":
                print(f"You have already learned {songs[song_number - 1][0]}")
            else:
                songs[song_number - 1][3] = "l"
                print(f"{songs[song_number - 1][0]} by {songs[song_number - 1][1]} learned")
        else:
            print("Invalid song number")
    except ValueError:
        print("Invalid input; enter a valid number.")

def display_songs_status(songs):
    print("Menu:")
    print("D - Display songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")
    print(">>> D")
    for i, song in enumerate(songs, start=1):
        status = "*" if song[3] == "u" else " "
        print(f"{i}. {status} {song[0]} by {song[1]} - {song[2]}")

def main():
    songs = load_songs()

    while True:
        display_songs(songs)
        choice = input(">>> ").upper()

        if choice == "D":
            display_songs_status(songs)
        elif choice == "A":
            add_song(songs)
        elif choice == "C":
            complete_song(songs)
        elif choice == "Q":
            save_songs(songs)
            print(f"{len(songs)} songs saved to songs.csv")
            print("Make some music!")
            break
        else:
            print("Invalid menu choice")

if __name__ == "__main__":
    main()