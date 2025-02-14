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
            if search in lines[0].lower().strip():
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
            if search in lines[0].lower().strip():
                output.append(f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.')
        
        if not output:
            print('Director not found.')
        else:
            print(f'Here is a list of movies with the director of: {search}.')
            for info_line_director in output:
                print(info_line_director)

def genre_search(output):
    with open("movie_recommender\Movies_list.csv", newline='') as file:
        movieCSV = csv.reader(file)
        next(movieCSV, None)
        search = input('Enter a genre to search for: ')
        output = []
        for lines in movieCSV:
            if search in lines[2].lower().strip():
                output.append(f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.')
        
        if not output:
            print('Genre not found.')
        else:
            print(f'Here is a list of movies with the director of: {search}.')
            for info_line_genre in output:
                print(info_line_genre)

def filter_both():
    with open("movie_recommender\Movies_list.csv", newline='') as file:
        movieCSV = csv.reader(file)
        next(movieCSV, None)
        search = input('Enter a director to search for: ')
        output = []
        for lines in movieCSV:
            if search in lines[0].lower().strip():
                output.append(f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.')
        
        if not output:
            print('Director not found.')

        search_genre = input('Enter a genre to search for: ')
        output_genre = []
        for lines in output:
            if search_genre in lines[2].lower().strip():
                output.append(f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.')
        
        if not output:
            print('Genre not found.')

    for lines in output_genre:
        print(lines)
        


def main():
    while True:
        choice = input("""
Here are your choices:

1: Search for a movie
2: Search for a director
3: Search for a genre
4: Filter a genre and a director
5: Get movie recommendations based off director/genre
6: Display the whole movie list
7: Exit the program
                       
Enter 1, 2, 3, 4, 5, or 6: """)
        
        if choice == '1':
            title_search()
        elif choice == '2':
            director_search()
        elif choice == '3':
            genre_search()
        elif choice == '4':
            filter_both()
        elif choice == '5':
            genre_or_director = input('Do you want to get recommendations based off of genre or director? (g or d): ')
            if genre_or_director == 'g':
                genre_search
            elif genre_or_director == 'd':
                genre_search
            else:
                print('Incorrect option.')
        elif choice == '6':
            with open("movie_recommender\Movies_list.csv", newline='') as file:
                movieCSV = csv.reader(file)
                next(movieCSV, None)
                for line in movieCSV:
                    print(line)
        elif choice == '7':
            print('Thanks for using the program!')
            break


main()