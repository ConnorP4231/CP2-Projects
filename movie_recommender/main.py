# Connor Pavicic, movie_recommender

"""Requirements:
-Uses the csv file for the movie list
-User is able to choose at least 2 filters for the program to search through
-User can get recommendations based on genre, directors, length and/or actors
-User is able to print the whole list"""

import csv

with open("movie_recommender\Movies list.csv", mode='r'):
    movieCSV = csv.reader()
    for lines in movieCSV:
        print(lines)