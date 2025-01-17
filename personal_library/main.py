# Connor Pavicic, personal_library

# What the program will do:
# Have users add different music artists to the set
# Have users remove different music artists
# Have users search for artists by genre or name

artists = []

def add_artist(artists=artists):
    artist = input('Enter an artist: ').lower()
    genre = input('Enter a genre: ').lower()
    artist_bio = ('Artist:', artist, ', Genre:', genre)
    artist_bio = ' '.join(artist_bio)
    artists.append(artist_bio)

def search():
    search_list = []
    search = input('Enter an artist/genre to search for: ')

    for x in artists:
        if search in x:
            search_list.append(x)
    
    if not search_list:
        print('Artist/Genre not found.')
    elif search_list:
        print(search_list)

def remove_artist(artists=artists):
    remove = input('Enter an artist that you would like to remove from the list: ')
    
    remove_text = ''
    for x in artists:
        if search in x:
            remove_text += x
    
    if not remove_text:
        print('Artist/Genre not found.')
    elif remove_text:
        print(f'Are you sure you want to remove this artist: {remove_text}')
    

def main():
    add_artist()
    search()

main()