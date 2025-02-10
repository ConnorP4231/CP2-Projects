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