# Connor Pavicic, clear_file

def clear_file():
    with open("word_counter/main_text.txt", "w") as file: #Opens file
        file.write("") #Writes the file to nothing which resets it.