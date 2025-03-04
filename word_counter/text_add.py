# Connor Pavicic, text_add

from time_handling import format_time # Gets the time from time handling function

def text_add():
    with open("word_counter/main_text.txt", "a") as file: #Opens the file
        add = input('Enter what you want to add: ')
        file.write('\n')
        file.write(add) #writes what the user added
        file.write("\n") #new line
        file.write('The time this was added: ')
        file.write(format_time) #Shows the time it was added
        return f"\n'{add}' was successfully added."