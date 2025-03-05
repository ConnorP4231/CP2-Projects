# Connor Pavicic, word_counter

from time_handling import format_time #Imports the time from time file.
from file_handling import

def word_counter():
    with open("word_counter/main_text.txt", "r+") as file: #Opens the file
        text = file.read() #Reads it
        count = len(text.split()) #Finds the word count

        if count == 0:
            file.write(f'\nWord Count Last Checked at: {format_time}.') #It still updates the time.
            return "\nThere are no words in the document." #If the word count is 0 then it returns that there is nothing.
        else:
            file.write(f'\nWord Count Last Checked at: {format_time}.') #Updates time
            return f"\nWord Count: {count}." #Prints word count