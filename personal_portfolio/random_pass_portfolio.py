import random #Gets random

# Collects user inputs for character counts
def get_user_inputs(pass_length):
    while True:
        try:
            num_upper = int(input('How many upper case letters do you want?: '))
            if num_upper > pass_length:
                print(f'You cannot have {num_upper} letters in a {pass_length}-character long password.') #makes sure it isn't longer than password length (same with all the others.)
            else:
                break
        except ValueError: #makes sure it is an int (same with all the others)
            print('That is not a correct input. Please enter a valid integer.')

    while True:
        try:
            num_lower = int(input('How many lower case letters do you want?: '))
            if num_upper + num_lower > pass_length:
                print(f'Too many characters to fit in a {pass_length}-character long password.')
            else:
                break
        except ValueError:
            print('That is not a correct input. Please enter a valid integer.')

    while True:
        try:
            num_num = int(input('How many numbers do you want?: '))
            if num_upper + num_lower + num_num > pass_length:
                print(f'Too many characters to fit in a {pass_length}-character long password.')
            else:
                break
        except ValueError:
            print('That is not a correct input. Please enter a valid integer.')

    while True:
        try:
            special_num = int(input('How many special characters do you want?: '))
            if num_upper + num_lower + num_num + special_num > pass_length:
                print(f'Too many characters to fit in a {pass_length}-character long password.')
            else:
                break
        except ValueError:
            print('That is not a correct input. Please enter a valid integer.')

    return num_upper, num_lower, num_num, special_num #returns all the values to be used later


# Generates x amount of random uppercase letters
def upper_case(password, num_upper):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for _ in range(num_upper):
        password.append(random.choice(letters))

# Generates x amount of lowercase letters
def lower_case(password, num_lower):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(num_lower):
        password.append(random.choice(letters))

# Generates x amount of numbers
def numbers(password, num_num):
    digits = '0123456789'
    for _ in range(num_num):
        password.append(random.choice(digits))

# Generates x amount of special characters
def special_character(password, special_num):
    special_chars = '!@#$%^&*'
    for _ in range(special_num):
        password.append(random.choice(special_chars))

# Makes sure the password meets length requirements
def fill(password, pass_length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(pass_length - len(password)):
        password.append(random.choice(letters))


# Main function that makes the password
def generate_password(pass_length, num_upper, num_lower, num_num, special_num):
    password = []
    # The function calls with each parameter set up.
    upper_case(password, num_upper)
    lower_case(password, num_lower)
    numbers(password, num_num)
    special_character(password, special_num)

    # Runs the filler function if length requirements aren't met.
    if len(password) < pass_length:
        fill(password, pass_length)

    #Shuffles the password in a random order
    random.shuffle(password)
    return ''.join(password) #Returns it


def password_main():
    # Gets the password length from the user
    while True:
        try:
            pass_length = int(input('How many characters do you want your password to be?: '))
            break
        except ValueError: #makes sure that it is an int.
            print('That is not a correct input. Please enter a valid integer.')

    #Gets 4 different outputs for the same requirements and prints them.
    num_upper, num_lower, num_num, special_num = get_user_inputs(pass_length)

    print("\nHere are your generated passwords:")
    for i in range(4):
        print(f"Password {i + 1}: {generate_password(pass_length, num_upper, num_lower, num_num, special_num)}")