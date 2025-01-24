# Connor Pavicic, random_pass

# What this program will do:
# Have users choose what they need in their password
# Have users choose how many of that thing will be in their password
# Arrange those things so that it sort of looks like

import random

pass_length = int(input('How many characters do you want your password to be?: '))
password = []

while True:
    num_upper = int(input('How many upper case letters do you want?: '))
    if num_upper>pass_length:
        print(f'You can not have {num_upper} letters in a {pass_length} character long password.')
    else:
        break

while True:
    num_lower = int(input('How many lower case letters do you want?: '))
    if num_lower + num_upper>pass_length:
        print(f'Too many characters to fit in a {pass_length} character long password.')
    else:
        break

while True:
    num_num = int(input('How many numbers do you want?: '))
    if num_num + num_lower + num_upper>pass_length:
        print(f'Too many characters to fit in a {pass_length} character long password.')
    else:
        break

while True:
    special_num = int(input('How many special characters do you want?: '))
    if special_num+num_num + num_lower + num_upper>pass_length:
        print(f'Too many characters to fit in a {pass_length} character long password.')
    else:
        break

def upper_case(password = password, num_upper = num_upper):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for letter in range(num_upper):
        letter = random.choice(letters)
        password.append(letter)



def lower_case(password = password, num_lower = num_lower):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in range(num_lower):
        letter = random.choice(letters)
        password.append(letter)


def number(password=password, num_num = num_num):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for number in range(num_num):
        number = random.choice(numbers)
        password.append(number)


def special_character(password = password, special_num = special_num):
    characters = ['!', '@', '#', '$', '%', '^', '&', '*']
    for char in range(special_num):
        char = random.choice(characters)
        password.append(char)


def fill(password = password):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in range(pass_length-len(password)):
        letter = random.choice(letters)
        password.insert(0, letter)

def main(password = password):
    upper_case()
    lower_case()
    special_character()
    number()
    password = ' '.join(password)
    final_pass = password.replace(' ', '')
    if special_num+num_num + num_lower + num_upper>pass_length < pass_length:
        fill()
    print(final_pass)

main()