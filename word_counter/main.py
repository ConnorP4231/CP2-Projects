# Connor Pavicic, word_counter

from text_add import text_add #imports the function for adding text
from word_counter import word_counter #imports the function for writing
from display_file import display_file #imports the function for displaying the file
from clear_file import clear_file #imports the function for clearing the file
from file_handling import file_handling #imports the function for file handling

def main():
    while True:
        #I remembered not to do multiline stuff
        choice = input("""\nWhich one would you like to do?:\n\n1. Choose your text file\n2. Display the current text file\n3. Add to the text file\n4. Find the word count of the text file\n5. Reset the file\n6. Exit the program\n\n(1, 2, 3, or 4): """)
        
        if choice == '1':
            print(file_handling())
        elif choice == '2':
            print(display_file()) #Runs the display file function
        elif choice == '3':
            print(text_add()) #Runs text add function
        elif choice == '4':
            print(word_counter()) #Runs word counter function
        elif choice == '5':
            clear_file() #Runs clear file function
            print('Successfully cleared file.')
        elif choice == '6':
            print('\nThanks for using this. Have a good day.')
            break
        else:
            print("\nIncorrect option, try again.") #Idiot proof

if __name__ == "__main__": #Since we're using multiple files I make sure the name is main.
    main()