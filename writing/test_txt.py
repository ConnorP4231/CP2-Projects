"""
Connor Pavicic, writing to text notes 

How do you find a file in a folder? 
    The file path will show you which files are in a folder. (You can go to file explorer for this too).
In a python project how do you open a file?
    with open("folder/file", "r") as file:
What is the difference between writing, appending, and creation modes?
    -Writing is where you actually write what is on the file and replace the other text.
    -Appending is adding to the file.
    -Creation modes is opening and creating a file.
    """

"""
r = to read the file
w = write on the file
(replaces the old file)
w+ = read and write
a = append (adds, doesn't delete)
x = create a file
a+ = append and read"""

import csv

data = [
    {"username": "yes", "color": "blue"},
    {"username": "sigmaboy123", "color": "teal"}
]

with open("writing/test.csv", "w+", newline="") as file:
    fieldnames = ["username", "color"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open("writing/test.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)