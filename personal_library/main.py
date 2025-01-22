# Connor Pavicic, personal_library

# What the program will do:
# Have users add different music artists to the set
# Have users remove different music artists
# Have users search for artists by genre or name

artists = [] # The main list that stores the artists

def add_artist(artists=artists): # The function that adds an artist to the list
    artist = input('Enter an artist: ').lower()
    genre = input('Enter a genre: ').lower()
    artist_bio = ('Artist:', artist, ', Genre:', genre) #This is the tuple that I used.
    artist_bio = ' '.join(artist_bio)
    artists.append(artist_bio)
    print('Artist added!')

def search(artists=artists): #This is the function to search for the artists.
    search_list = []
    search = input('Enter an artist/genre to search for: ')

    for x in artists: #Goes through each value of the artist list and if it is equal to the search then it puts it into a new list.
        if search in x:
            search_list.append(x)
    
    if not search_list:
        print('Artist/Genre not found.')
    elif search_list:
        print(search_list)

def remove_artist(artists=artists): #This is the function to remove an artist.
    remove = input('Enter an artist that you would like to remove from the list (you can search their genre to identify them): ').lower()

    
    remove_list = [x for x in artists if remove in x.lower()] # A little bit different style of code since I have to remove the artist.

    if not remove_list:
        print('Artist/Genre not found.')
        return

    # If their search pulls up multiple artists: 
    while len(remove_list) > 1:
        print(f'Multiple matches found: {remove_list}')
        remove_again = input('Please specify the exact artist you want to remove: ').lower()
        remove_list = [x for x in remove_list if remove_again in x.lower()]

        if not remove_list:
            print('No matches found for your input. Exiting removal process.')
            return

    
    artist_to_remove = remove_list[0]
    are_you_sure = input(f'Are you sure that you want to remove this artist: "{artist_to_remove}"? (yes/no): ').lower() #Makes sure the user actually wants to remove the specified artist.

    if are_you_sure == 'yes':
        artists.remove(artist_to_remove)
        print('Artist deleted.')
    elif are_you_sure == 'no':
        print('Operation canceled. The artist was not removed.')
    else:
        print('Invalid option. The artist is still in the list.')

    

def main(): #The main function that runs all the other functions based off what the user wants.
    while True:
        options = input("""
Options: 

1. Add an artist
2. Remove an artist
3. Search for an artist
4. Look at the artist list
5. Exit the program

Which one would you like to do? (1, 2, 3, 4, or 5): """)

        if options == '1':
            add_artist()
        elif options == '2':
            remove_artist()
        elif options == '3':
            search()
        elif options == '4': #They can look at their artist list.
            print(artists)
        elif options == '5': #They can exit the program
            print('Thanks for using the program!')
            break
        else:
            print('Incorrect option, try again.')
            continue


main()