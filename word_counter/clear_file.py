# Connor Pavicic, clear_file

from file_handling import file_name

def clear_file():
    with open(file_name, "w") as file: #Opens file
        file.write("") #Writes the file to nothing which resets it.