<<<<<<< HEAD
#Evan McCabe Raidd: Number Guessing Game

# The goal of this project is to generate a number 1-10, have the user guess a number 1-10,
# and check if they match. It needs to choose a number, let the user guess a number, and then
# check if the two are identical. If they are, the program should tell them, and ask if they want
# to play again. Otherwise, the program should let them keep trying until they get it. Once
# the user guesses correctly, the program should tell them how many tries it took them.

# (Psuedocode was written, and then converted to actual code.)

#import random for number generation:
import random

#Make a list of valid guesses for the user to make and make sure it's globally available:
global validGuesses
validGuesses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#make the user's guesses globally accesible:
global guesses
#Set the user's intial number of guesses:
guesses = 0

#Intro Message:
print("\nHello! Welcome to the Number Guessing Game. \nYour goal is to guess which number 1 through 10 that I generate.")


#function for running the game:
def runGame():
    #Make sure the valid guesses variable can be accessed:
    global validGuesses
    #Make sure the guesses variable can be accessed:
    global guesses
    #Initialize the user's number of guesses to 0:
    guesses = 0
    #Pick the number for the user to guess:
    numToGuess = random.randint(1, 10)
    #Allow the user to guess the number:
    guess = input("\nI picked a number!\nWhat is your guess? ")
    #If the user's guess is not a number:
    try:
        1<= int(guess) <= 10
    except ValueError:
        guess = input("\nThat is an invalid input. Please try again. ")
    #if the input is invalid (not a number 1-10):
    if int(guess) not in validGuesses:
        guess = input("\nThat is an invalid input. Please try again. ")
    
    #if the user is right(less likely):
    if int(guess) == numToGuess:
        #Tell the user they've won, how many guesses they took, and ask if they'd like to play again:
        playAgain = input("\nCorrect! You win! XD\nYou guessed in 1 attempt.\n\nPlay again? (y for yes, n for no)\n")
        #if the user DOES want to play again:
        if playAgain == "y":
            #run the game again:
            runGame()
        #if the user DOES NOT want to play again:
        else:
            print("\nThanks for playing!\n")
            #stop the program:
            exit()
    #if the user is wrong(more likely):
    else:
        #Tell the user they got it wrong:
        print("\nWrong! DX")
        #add 1 to the number of user guesses:
        guesses += 1

        #Keep letting the user guess the number until they get it right:
        def wrong():
            #Make sure the valid guesses variable can be accessed:
            global validGuesses
            #Make sure the guesses variable can be accessed:
            global guesses
            #Add 1 to the number of guesses if the user is wrong:
            guesses += 1
            guess = input("What is your next guess? ")
            #If the user's guess is not a number:
            try:
              1<= int(guess) <= 10
            except ValueError:
              guess = input("\nThat is an invalid input. Please try again. ")
            #if the input is invalid (not a number 1-10):
            if int(guess) not in validGuesses:
              guess = input("\nThat is an invalid input. Please try again. ")
            #Check if the user got it right this time:
            #if they DID:
            if int(guess) == numToGuess:
                #Make sure that the number of guesses can be used in a print statement:
                guesses = str(guesses)
                #Tell the user they won, how many guesses they took, and ask if they want to play again:
                playAgain = input("\nCorrect! You win! XD\nYou guessed in " + guesses + " attempts.\n\nWould you like to play again (y for yes , n for no)\n")
                if playAgain == "y":
                #run the game again:
                  runGame()
                #if the user DOES NOT want to play again:
                else:
                  print("\nThanks for playing!\n")
                  #stop the program:
                  exit()
            #if they DID not guess correctly:
            else:
                #Tell the user they were wrong:
                print("\nWrong!")
                #Add 1 to the number of user guesses:\
                guesses += 1
                #run the function again so the user can keep guessing:
                wrong()
        #run the function to let the user try again:
        wrong()

#run the game:
runGame()

#Tester #1: Sam
#Does the program run?
# yes
#Did you do something that made the program stop working, if so then what?
# i guessed the number
#Were you able to use the program without any help from the programmer?
# yes
#If you needed further explanation on things, what explanations did you need?
# n/a

#Tester #2: 
#Does the program run?
# Yes.
#Did you do something that made the program stop working, if so then what?
# Winning made the program stop. Oh wait, no it didn't.
#Were you able to use the program without any help from the programmer?
# Yes, I was.
#If you needed further explanation on things, what explanations did you need?
# I did not need further explanation on anything.

#Improvements made after feedback:
# I clarified that the computer was generating a number 1 through 10
# I fixed a small error that caused the number of guesses printed to be incorrect
# I made sure that the code would keep running smoothly if the user made an invalid input.
=======
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
>>>>>>> 3525fa6e34342bd37307d095595e43c956df4bcb
