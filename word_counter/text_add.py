# Connor Pavicic, text_add

from time_handling import format_time

def text_add():
    with open("word_counter/main_text.txt", "w") as file:
        add = input('Enter what you want to add: ')
        file.write(add)
        file.write("\n")
        file.write(format_time)
        return f"\n'{add}' was successfully added."