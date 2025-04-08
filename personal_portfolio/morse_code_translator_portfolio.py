# Connor Pavicic, morse_code_translator

# list of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', 
           '4', '5', '6', '7', '8', '9']

# list of morse code characters
morse_codes = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', 
    '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', 
    '..-', '...-', '.--', '-..-', '-.--', '--..',
    '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.'
]

def english_to_morse(): # The function that changes english to morse code
    valid = False
    valid_chars = letters + [' ']
    while not valid:
        to_be_translated = input('What do you want to translate into morse code?: ').lower()
        if all(char in valid_chars for char in to_be_translated):
            valid = True
        else:
            print('Invalid characters found, try again.') #makes sure that the user input is valid.
    
    final_translation = ''
    
    for char in to_be_translated: #goes through each character in the list and then finds the index and takes the index in the morse code then adds it to a string.
        if char in letters:
            final_translation += morse_codes[letters.index(char)] + ' '
        elif char == ' ':
            final_translation += '/ '
    
    print(final_translation)

def morse_to_english(): #Function for morse code to English.
    valid = False
    valid_chars = ['.', '-', '/', ' ']
    while not valid:
        to_be_translated = input('What do you want to translate into English?: ')
        if all(char in valid_chars for char in to_be_translated):
            valid = True
        else:
            print('Invalid characters found, try again.') #makes sure the user is inputting something correct.
    
    final_translation = ''
    words = to_be_translated.split(' / ')
    
    for word in words: #does the same thing as the other function but the other way around.
        chars = word.split()
        for char in chars:
            if char in morse_codes:
                final_translation += letters[morse_codes.index(char)]
        final_translation += ' '
    
    print(final_translation.strip())

def morse_main(): #the main function that runs everything.
    while True:
        options = input("""
1: English to morse code
2: Morse code to English
3: Exit the program
                        
(1, 2, or 3): """)
        
        if options == '1':
            english_to_morse()
        elif options == '2':
            morse_to_english()
        elif options == '3':
            print('Thanks for using the program.')
            break
        else:
            print('Incorrect option, try again.')