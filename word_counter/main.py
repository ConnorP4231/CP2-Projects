# Connor Pavicic, word_counter

from text_add import text_add
from word_counter import word_counter
from display_file import display_file
from clear_file import 

def main():
    while True:
        choice = input("""\nWhich one would you like to do?:
                    
1. Display the current text file
2. Add to the text file
3. Find the word count of the text file
4. Reset the file
5. Exit the program
                
(1, 2, 3, or 4): """)
        
        if choice == '1':
            print(display_file())
        elif choice == '2':
            print(text_add())
        elif choice == '3':
            print(word_counter())
        elif choice == '4':

        elif choice == '5':
            print('\nThanks for using this. Have a good day.')
            break
        else:
            print("\nIncorrect option, try again.")

if __name__ == "__main__":
    main()