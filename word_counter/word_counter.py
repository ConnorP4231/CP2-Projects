# Connor Pavicic, word_counter

def word_counter():
    with open("word_counter/main_text.txt", "r") as file:
        text = file.read()
        count = len(text.split())

        if count == 0:
            return "\nThere are no words in the document."
        else:
            return f"\nWord Count Including Date: {count}. \nWord Count Excluding Date: {count-2}"


word_counter()