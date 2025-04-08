from financial_calculator_portfolio import financial_main
from morse_code_translator_portfolio import morse_main
from movie_recommender_portfolio import movie_main
from personal_library_portfolio import main_personal_library
from random_pass_portfolio import password_main
from to_do_list_portfolio import to_do_main


def main():
    print('\nThis is my personal portfolio. In here are six projects that I have created across this current spring semester in my computer science class.')
    print('\nTo use all of these programs, just follow the instructions displayed on screen and everything should be just fine. Enjoy these six programs.')
        
    while True:
        choice = input('\nWhich program would you like to use?:\n\n1. Financial Calculator\n2. Morse Code Translator\n3. Movie Recommender\n4. Personal Library\n5. Random Password Generator\n6. To Do List Maker\n7. Exit the program.\n\n(1-7): ')

        if choice == '1':
            print('\nThis project will: Set up savings goals based off your inputs, calculate compound interest, have a budget allocator, calculate sale price, calculate tips.')
            print('The programming process for this was like any other. I receive my instructions on what to do, and then I coded it, tested it, and submitted it.')
            print("I didn't really learn anything about coding, but some financial stuff I leanred, like a budget allocator, and the actual formula for compound interest.")
            print('Here is the program:\n')

            financial_main()

        elif choice == '2':
            print('\nThis project is a morse code translator. It can translate any text from English to morse code and vice versa.')
            print('The programming process for this was like any other. I receive my instructions on what to do, and then I coded it, tested it, and submitted it.')
            print('I accidentally learned around half the morse code alphabet in the process of creating this project, and it was really fun.')
            print('Here is the program:\n')

            morse_main()

        elif choice == '3':
            print('\nThis project takes a whole list of movies, and filters the movies based off of your inputs.')
            print('The programming process for this was like any other. I receive my instructions on what to do, and then I coded it, tested it, and submitted it.')
            print('I learned how to handle csv files from this program and it was really cool to learn how to do that.')
            print('Here is the program:\n')

            movie_main()

        elif choice == '4':
            print('\nThis program lets you add, remove, and search up music artists based off of their genre or name.')
            print('The programming process for this was like any other. I receive my instructions on what to do, and then I coded it, tested it, and submitted it.')
            print('I learned a lot about string manipulation by removing whitespace from the text and splitting it, and all that.')
            print('Here is the program:\n')

            main_personal_library()

        elif choice == '5':
            print('\nThis program generates you 4 random passwords based off your inputs.')
            print('The programming process for this was like any other. I receive my instructions on what to do, and then I coded it, tested it, and submitted it.')
            print("I didn't really learn much about this password since it was just randomly choosing characters and adding them to a string.")
            print('Here is the program:\n')

            password_main()

        elif choice == '6':
            print('\nThis program allows you to add, remove, or check off things on a to do list.')
            print('The programming process for this was like any other. I receive my instructions on what to do, and then I coded it, tested it, and submitted it.')
            print('In this project I learned a lot about text files and how to append to them and replace things.')
            print('Here is the program:\n')

            to_do_main()

        elif choice == '7':
            print('\nThanks for checking out my portfolio, have a good day.')
            break
        
        else:
            print('\nIncorrect option, try again.')

if __name__ == '__main__':
    main()