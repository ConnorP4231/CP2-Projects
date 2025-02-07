# Connor Pavicic, personal_library

print("""This is a program where you can add and remove artists to a list. You can also search for them too.
Currently, the list is empty, so do whatever you want.""")

artists = {}  # Use a dictionary instead of a list

def add_artist():
    artist = input('Enter an artist: ').strip().lower()
    genre = input('Enter a genre: ').strip().lower()
    
    if artist in artists:
        print(f"{artist.title()} is already in the library under {artists[artist].title()}.")
    else:
        artists[artist] = genre
        print(f'Artist "{artist.title()}" added under the genre "{genre.title()}".')

def search():
    search_term = input('Enter an artist or genre to search for: ').strip().lower()
    matches = {artist: genre for artist, genre in artists.items() if search_term in artist or search_term in genre}

    if not matches:
        print('Artist/Genre not found.')
    else:
        print("Search results:")
        for artist, genre in matches.items():
            print(f"{artist.title()} - {genre.title()}")

def remove_artist():
    remove_artist = input('Enter the artist you want to remove: ').strip().lower()  # Normalize input

    # Find artist in the dictionary with case-insensitive matching
    artist_found = None
    for artist in artists.keys():
        if artist.lower() == remove_artist:  # Match the lowercase version
            artist_found = artist
            break

    if artist_found:
        confirm = input(f'Are you sure you want to remove "{artist_found.title()}"? (yes/no): ').strip().lower()
        if confirm == 'yes':
            del artists[artist_found]
            print(f'Artist "{artist_found.title()}" deleted.')
        else:
            print('Operation canceled.')
    else:
        print('Artist not found.')

def main():
    while True:
        options = input("""
Options: 
1. Add an artist
2. Remove an artist
3. Search for an artist
4. Show artist list
5. Exit the program

Choose an option (1, 2, 3, 4, or 5): """).strip()

        if options == '1':
            add_artist()
        elif options == '2':
            remove_artist()
        elif options == '3':
            search()
        elif options == '4':
            if artists:
                print("\nCurrent Artist List:")
                for artist, genre in artists.items():
                    print(f"{artist.title()} - {genre.title()}")
            else:
                print("The artist list is currently empty.")
        elif options == '5':
            print('Thanks for using the program!')
            break
        else:
            print('Invalid option, try again.')

main()
