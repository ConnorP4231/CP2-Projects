# Connor Pavicic, Reading Notes Python
import csv

file = open("test/test.txt", "r").read()

users = {}

with open("test/user_info.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)