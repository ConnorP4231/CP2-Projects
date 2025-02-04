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
    valid = False
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890 "
    while valid == False:
        to_be_translated = input('What do you want to translate into morse code?: ')
        if all(char in valid_chars for char in to_be_translated):
            valid = True
        else:
            print('Invalid characters found, try again.')
    
    final_translation = ''

    for x in to_be_translated:
        if x in translation_dict:
            final_translation += translation_dict[x]
            final_translation += ' '
        elif x == ' ':
            final_translation += '/ '
    
    print(final_translation)


def morse_to_english():
    valid = False
    valid_chars = './- '
    while valid == False:
        to_be_translated = input('What do you want to translate into English?: ')
        if not any(char in valid_chars for char in to_be_translated):
            print('Invalid characters found, try again.')
        else:
            valid = True
        
        final_translation = ''

        for x in to_be_translated:
            if x in reversed_translation_dict:
                final_translation += reversed_translation_dict[x]
            elif x == '/':
                final_translation += ' '

        print(final_translation)


morse_to_english()