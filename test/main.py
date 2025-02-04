# Connor Pavicic, morse_code_translator

translation_dict = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.', 
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---', 
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---', 
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',  't': '-', 
    'u': '..-',   'v': '...-', 'w': '.--',   'x': '-..-',  'y': '-.--', 
    'z': '--..',  

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

reversed_translation_dict = {
    '.-': 'a',   '-...': 'b',   '-.-.': 'c',   '-..': 'd',   '.': 'e', 
    '..-.': 'f', '--.': 'g',   '....': 'h',   '..': 'i',    '.---': 'j', 
    '-.-': 'k',  '.-..': 'l',  '--': 'm',    '-.': 'n',    '---': 'o', 
    '.--.': 'p', '--.-': 'q',  '.-.': 'r',   '...': 's',   '-': 't', 
    '..-': 'u',  '...-': 'v',  '.--': 'w',   '-..-': 'x',  '-.--': 'y', 
    '--..': 'z',  

    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
}


def english_to_morse():
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890 "
    while True:
        to_be_translated = input('What do you want to translate into Morse code? (Only letters, digits, and spaces allowed): ')
        if all(char in valid_chars for char in to_be_translated):
            break
        else:
            print('Invalid characters found. Please only use letters, digits, and spaces.')
    
    final_translation = ''

    for x in to_be_translated:
        if x in translation_dict:
            final_translation += translation_dict[x] + ' '
        elif x == ' ':
            final_translation += '/ '  # This represents space in Morse code

    print("Morse Code Translation:", final_translation.strip())


def morse_to_english():
    valid_chars = './- '
    while True:
        to_be_translated = input('What do you want to translate into English? (Only Morse code symbols ./- and spaces allowed): ')
        # Check that all characters in the input are valid Morse symbols or spaces
        if all(char in valid_chars for char in to_be_translated):
            break
        else:
            print('Invalid characters found. Please only use ./- and spaces.')

    # Remove extra spaces and split by '/'
    to_be_translated = to_be_translated.strip().replace('  ', ' ').split(' ')

    final_translation = ''

    for x in to_be_translated:
        if x in reversed_translation_dict:
            final_translation += reversed_translation_dict[x]
        elif x == '/':
            final_translation += ' '

    print("English Translation:", final_translation.strip())


# Test the functions
while True:
    mode = input("Choose mode:\n1. Translate English to Morse Code\n2. Translate Morse Code to English\n3. Quit\n")
    if mode == '1':
        english_to_morse()
    elif mode == '2':
        morse_to_english()
    elif mode == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")