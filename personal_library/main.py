# Connor Pavicic, personal_library

# What the program will do:
# Have users add different music artists to the set
# Have users remove different music artists
# Have users search for artists by genre or name

artists = []

for x in range(2):
    artist = input('Enter an artist: ')
    genre = input('Enter a genre: ')
    artist_bio = {'Artist:', artist, 'Genre:', genre}
    artist_bio = ' '.join(artist_bio)
    artists.append(artist_bio)

