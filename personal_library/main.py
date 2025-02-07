from datetime import datetime #Tracks the date and time

# Connor Pavicic, personal_library

print("""This is a program where you can add and remove artists to a list. You can also search for them too.
Currently, the list is empty, so do whatever you want.""")

artists = {}  # Use a dictionary instead of a list

def add_artist():  # Function to add artists
    artist = input('Enter an artist: ').strip().lower()
    genre = input('Enter a genre: ').strip().lower()
    date_added = datetime.now().strftime("%Y-%m-%d") #Gets the date
    time_added = datetime.now().strftime("%H:%M:%S") #Gets the time
    
    if artist in artists:  # Makes sure that this is a new artist.
        print(f"{artist.title()} is already in the library under {artists[artist]['genre'].title()}.")
    else:
        artists[artist] = {"genre": genre, "date_added": date_added, "time_added": time_added}  # Stores artist with genre, date, and time
        print(f'Artist "{artist.title()}" added under the genre "{genre.title()}" on {date_added} at {time_added}.')

def search():  # The function that searches for artists.
    search_term = input('Enter an artist or genre to search for: ').strip().lower()
    matches = {artist: info for artist, info in artists.items() if search_term in artist or search_term in info["genre"]}  # Goes through the dictionary to find matches.

    if not matches:  # If no matches are found
        print('Artist/Genre not found.')
    else:
        print("Search results:")
        for artist, info in matches.items():  # Prints the found items.
            print(f"{artist.title()} - {info['genre'].title()} (Added on {info['date_added']} at {info['time_added']})")

def remove_artist():  # The function that removes artists.
    remove_artist = input('Enter the artist you want to remove: ').strip().lower()

    # Finds artist in dictionary
    artist_found = None
    for artist in artists.keys():
        if artist.lower() == remove_artist:  # Match the lowercase version
            artist_found = artist
            break

    if artist_found:
        confirm = input(f'Are you sure you want to remove "{artist_found.title()}"? (yes/no): ').strip().lower()
        if confirm == 'yes':
            del artists[artist_found]  # Deletes the artist
            print(f'Artist "{artist_found.title()}" deleted.')
        else:
            print('Operation canceled.')  # If they chose not to, it just prints this.
    else:  # If the artist isn't found:
        print('Artist not found.')

def main():  # The main function that asks the user what they want to do.
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
            if artists:  # Prints the artist list.
                print("\nCurrent Artist List:")
                for artist, info in artists.items():
                    print(f"{artist.title()} - {info['genre'].title()} (Added on {info['date_added']} at {info['time_added']})")
            else:
                print("The artist list is currently empty.")
        elif options == '5':
            print('Thanks for using the program!')
            break
        else:  # Ensures the user types a correct input.
            print('Invalid option, try again.')

main()
