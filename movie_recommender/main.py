# Connor Pavicic, movie_recommender

"""Requirements:
-Uses the csv file for the movie list
-User is able to choose at least 2 filters for the program to search through
-User can get recommendations based on genre or actors
-User is able to print the whole list"""

import csv

def title_search():
    with open("movie_recommender\Movies_list.csv", newline='') as file:
        movieCSV = csv.reader(file)
        next(movieCSV, None)
        search = input('Enter a movie to search for: ')
        output = ''
        for lines in movieCSV:
            if lines[0].lower() == search:
                output += f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.'
        
        if output == '':
            print('Movie not found.')
        else:
            print(output)

def director_search():
    with open("movie_recommender\Movies_list.csv", newline='') as file:
        movieCSV = csv.reader(file)
        next(movieCSV, None)
        search = input('Enter a director to search for: ')
        output = []
        for lines in movieCSV:
            if lines[1].lower() == search:
                output.append(f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.')
        
        if not output:
            print('Director not found.')
        else:
            print(f'Here is a list of movies with the director of: {search}.')
            for info_line in output:
                print(info_line)

def genre_search():
    with open("movie_recommender\Movies_list.csv", newline='') as file:
        movieCSV = csv.reader(file)
        next(movieCSV, None)
        search = input('Enter a genre to search for: ')
        output = []
        for lines in movieCSV:
            if search in lines[2].lower():
                output.append(f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.')
        
        if not output:
            print('Genre not found.')
        else:
            print(f'Here is a list of movies with the director of: {search}.')
            for info_line in output:
                print(info_line)

genre_search()

def main():
    while True:
        choice = input("""
Here are your choices:

1: Search for a movie
2: Search for a director
3: Search for a genre
4: Get movie recommendations based off director/genre
5: Display the whole movie list
6: Exit the program
                       
Enter 1, 2, 3, 4, 5, or 6: """)
        
        if choice == '1':
            title_search()
        elif choice == '2':
            director_search()
        elif choice == '3':
            genre_search()
        elif choice == '4':
            genre_or_director = input('Do you want to get recommendations based off of genre or director? (g or d): ')
            if genre_or_director == 'g':
                genre_search
            elif genre_or_director == 'd':
                genre_search
            else:
                print('Incorrect option.')
        elif choice == '5':
            with open("movie_recommender\Movies_list.csv", newline='') as file:
                movieCSV = csv.reader(file)
                next(movieCSV, None)
                print(movieCSV)
        elif choice == '6':
            print('Thanks for using the program!')
            break


main()