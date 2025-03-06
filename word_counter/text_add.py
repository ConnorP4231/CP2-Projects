# Connor Pavicic, text_add

from time_handling import format_time # Gets the time from time handling function
from file_handling import file_name

def text_add(file_name):
    with open(file_name, "a") as file: #Opens the file
        add = input('Enter what you want to add: ')
        file.write('\n')
        file.write(add) #writes what the user added
        file.write("\n") #new line
        file.write('The time this was added: ')
        file.write(format_time) #Shows the time it was added
        return f"\n'{add}' was successfully added."