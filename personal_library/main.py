# Connor Pavicic, personal_library

# What the program will do:
# Have users add different music artists to the set
# Have users remove different music artists
# Have users search for artists by genre or name

artists = []

artist = input('Enter an artist: ')
genre = input('Enter a genre: ')
artist_bio = ('Artist:', artist, ', Genre:', genre)
artist_bio = ' '.join(artist_bio)
artists.append(artist_bio)

print(artists)

search = input('Enter an artist to search for: ').lower()

search_list = []
for i in artists:
    if search in i:
        search_list.append(i)

if not search_list:
    