# Connor Pavicic, random_pass

# What this program will do:
# Have users choose what they need in their password
# Have users choose how many of that thing will be in their password
# Arrange those things so that it sort of looks like

import random

pass_length = int(input('How many characters do you want your password to be?: '))

def upper_case():
    num_upper = int(input('How many upper case letters do you want?: '))
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
