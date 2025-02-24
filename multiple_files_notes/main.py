#Connor Pavicic, Multiple Python pages notes

#1. How do you make multiple files in python?
    # Make a new file ending in .py
    # snake case file names 
    # descriptive file names (short)

#2. How do you get a function from another file
    # * lets you import everything
from calc import addition as add, subtraction as sub, num
    #alising is where you import a function and give it a new keyword

print(add())
print(sub(num, 4))

#3. How do you get variables from another file?
    # Same thing as functions, but is not advised to import a variable.
from calc import num
#better to return from a function

#4. How do you have a function with multiple returns?
def get_user_info():
    name = input("What is your name:\n")
    age = input("What is your age:\n")
    color = input("What is your favorite color:\n")
    return name, age, color

n, a, c = get_user_info()
print(n)
#Use commas to separate each item you want to return.

#5. Why would you use multiple pages for a python project? 
    # It is easier to merge github branches.
    # Modularity - breaking the program into smaller more managable pieces.
    # Main should only include the introduction stuff to your project and your user interface.
    # Functionality - specific functions used in multiple locations will get their own page so that they do not get mixed up with the rest of your code

    # if multiple pages then
    # if __name__ == "main":
    #   multiplication(5,2)