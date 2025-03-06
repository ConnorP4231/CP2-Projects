# Connor Pavicic, file_handling

def file_handling():
    while True:
        file_name = input('What is the relative path of your file?: ') #asks for the relative path
        try:
            with open(file_name, "r") as file: #Sees if it can open without error
                return file_name  # Return valid file
        except FileNotFoundError: #If the file is not found then it says that it doesn't exist.
            print("File does not exist. Please enter a valid file.")  # Keep asking

file_name = file_handling() #Gets the file_name so the other functions can work properly