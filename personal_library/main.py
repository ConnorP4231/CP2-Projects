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
    print('Artist added!')

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
    
    remove_list = []
    for x in artists:
        if remove in x:
            remove_list += x
    
    if not remove_list:
        print('Artist/Genre not found.')
    elif remove_list:
        while len(remove_list) > 1:
            remove_again = input(f'Which one of these artists: {remove_list} would you like to remove: ')
            remove_list = []
            for x in artists:
                if remove_again in x:
                    remove_list += x    
        
        str(remove_list)
        are_you_sure = input(f'Are you sure that you want to remove this artist: {remove_list}').lower()
        
        if are_you_sure == 'yes':
            artists.remove(remove_list)
            print('Artist deleted.')
        elif are_you_sure == 'no':
            pass
        else:
            print('Incorrect option. The artist is still in the list.')
    

def main():
    options = input("""
Options: 

1. Add an artist
2. Remove an artist
3. Search for an artist

Which one would you like to do? (1, 2, or 3): """)

    if options == 1:
        add_artist()
    elif options == 2


main()