# Connor Pavicic, display_file

def display_file():
    with open("word_counter/main_text.txt", "r") as file: #Opens the file
        text = file.read() #Reads the file to turn it into a string.
        
        if not text.strip(): #Gets rid of all spaces and tabs and then sees if there is anything in it.
            return "\nThere is nothing in the text file." #If not then it returns there is nothing.
        else:
            return f"\n{text}" #Returns the text