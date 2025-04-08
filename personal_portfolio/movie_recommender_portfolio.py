# Connor Pavicic, movie_recommender

import csv #imports csv

def title_search(): #function of searching for a movie name.
    with open("personal_portfolio/Movies_list_portfolio.csv", newline='') as file: #gets the csv file
        movieCSV = csv.reader(file)
        next(movieCSV, None) #skips the next line so it doesn't print what each category is.
        search = input('Enter a movie to search for: ').strip().lower()
        found = False
        
        for lines in movieCSV:
            if search in lines[0].lower():
                print(f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, '
                      f'has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.') #prints the movie.
                found = True #if something is found then it sets found to true.
        
        if not found:
            print('Movie not found.')

def director_search(): #function for director search (does the same thing as last function but with different lines)
    with open("personal_portfolio/Movies_list_portfolio.csv", newline='') as file:
        movieCSV = csv.reader(file)
        next(movieCSV, None)
        search = input('Enter a director to search for: ').strip().lower()
        output = []
        
        for lines in movieCSV:
            if search in lines[1].lower():
                output.append(f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, '
                              f'has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.')
        
        if output:
            print(f'Here is a list of movies directed by {search}:')
            for movie in output:
                print(movie)
        else:
            print('Director not found.')

def genre_search(): #the function for searching for a genre. (does the same thing as the last 2 but with different lines).
    with open("personal_portfolio/Movies_list_portfolio.csv", newline='') as file:
        movieCSV = csv.reader(file)
        next(movieCSV, None)
        search = input('Enter a genre to search for: ').strip().lower()
        output = []
        
        for lines in movieCSV:
            if search in lines[2].lower():
                output.append(f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, '
                              f'has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.')
        
        if output:
            print(f'Here is a list of movies in the {search} genre:')
            for movie in output:
                print(movie)
        else:
            print('Genre not found.')

def filter_both(): #the function for filtering both genre and director. (does the same thing as last functions but use both genre and director in the for loop when searching through each line.
    with open("personal_portfolio/Movies_list_portfolio.csv", newline='') as file:
        movieCSV = csv.reader(file)
        next(movieCSV, None)
        director_search = input('Enter a director to search for: ').strip().lower()
        genre_search = input('Enter a genre to search for: ').strip().lower()
        output = []
        
        for lines in movieCSV:
            if director_search in lines[1].lower() and genre_search in lines[2].lower():
                output.append(f'The movie: {lines[0]}, was directed by: {lines[1]}, has the genre of: {lines[2]}, '
                              f'has the rating of: {lines[3]}, is {lines[4]} minutes long, and here are notable actors: {lines[5]}.')
        
        if output:
            print(f'Here are movies directed by {director_search} in the {genre_search} genre:')
            for movie in output:
                print(movie)
        else:
            print('No matching movies found.')

def display_all_movies(): #This is the function for printing all the movies.
    with open("personal_portfolio/Movies_list_portfolio.csv", newline='') as file:
        movieCSV = csv.reader(file)
        next(movieCSV, None)
        
        for line in movieCSV: #this just goes through each line and prints it.
            print(', '.join(line))

def movie_main(): #the main function that allows the user to input what function they want to run.
    while True:
        choice = input("""
Here are your choices:

1: Search for a movie
2: Search for a director
3: Search for a genre
4: Filter by director and genre
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
            filter_both()
        elif choice == '5':
            display_all_movies()
        elif choice == '6':
            print('Thanks for using the program!')
            break
        else:
            print('Invalid option, please try again.')