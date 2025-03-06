# Connor Pavicic, word_counter

from text_add import text_add #imports the function for adding text
from word_counter import word_counter #imports the function for writing
from display_file import display_file #imports the function for displaying the file
from clear_file import clear_file #imports the function for clearing the file
from file_handling import file_handling #imports the function for file handling

def main():
    file_name = file_handling()  # Store the filename

    if file_name == "File does not exist.":  # Stop execution if file is missing
        print(file_name)
        return  

    while True:
        choice = input("""\nWhich one would you like to do?:\n\n1. Display the current text file\n2. Add to the text file\n3. Find the word count of the text file\n4. Reset the file\n5. Exit the program\n\n(1, 2, 3, 4, or 5): """)

        if choice == '1':
            print(display_file(file_name))  # Pass valid file name
        elif choice == '2':
            print(text_add(file_name))  
        elif choice == '3':
            print(word_counter(file_name))  
        elif choice == '4':
            clear_file(file_name)  
            print('Successfully cleared file.')
        elif choice == '5':
            print('\nThanks for using this. Have a good day.')
            break
        else:
            print("\nIncorrect option, try again.")

if __name__ == "__main__":
    main()