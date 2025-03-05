# Connor Pavicic, file_handling

def file_handling():
    try:
        file_name = input('What is the relative path of your file?: ')
        with open(file_name, "r") as file:
            return file_name
    
    except FileNotFoundError:
        return "File does not exist."