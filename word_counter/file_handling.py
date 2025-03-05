# Connor Pavicic, file_handling

def file_handling():
    try:
        file_name1 = input('What is the relative path of your file?: ')
        with open(file_name1, "r") as file:
            return file_name1
    
    except FileNotFoundError:
        return "File does not exist."
    
file_name = file_handling()
print(file_name)