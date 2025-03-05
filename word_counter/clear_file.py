# Connor Pavicic, clear_file

from file_handling import file_handling

def clear_file():
    with open("", "w") as file: #Opens file
        file.write("") #Writes the file to nothing which resets it.