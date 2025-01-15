# Connor Pavicic, personal_library

# What the program will do:
# Have users add different music artists to the set
# Have users remove different music artists
# Have users search for artists by genre, name, or a song name

artists = {}

def add_artist():
    for x in range(2):
        artist = input('Enter an artist name that you would like to enter: ')
        genre = input('Enter the genre that their music style is: ')
        song = input('Enter a specific song of theirs if you want to search them easier. (Leave this blank if you do not want to.): ')

        artist_bio = (artist, genre, song)

    artists.add(artist_bio)
    print(artists)

add_artist()