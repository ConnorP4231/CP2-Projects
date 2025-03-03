# Connor Pavicic, display_file

def display_file():
    with open("word_counter/main_text.txt", "r") as file:
        text = file.read()
        
        if not text.strip():
            return "\nThere is nothing in the text file."
        else:
            for line in text:
                return f"\n{text}"