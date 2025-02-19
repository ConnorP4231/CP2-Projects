# Connor Pavicic, to_do_list

"""What this program will do:

Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list"""


def add_item():
    with open("to_do_list/main.txt", "a", newline="") as file:
        task = input('What task do you need to do?: ')
        to_be_appended = task + ": Not done yet."
        file.write("\n"+to_be_appended)

def mark_as_complete():
    to_be_replaced = input('What text do you want to replace?: ')
    to_be_replaced_with = input(f'What do you want to replace {to_be_replaced} with?: ')
     

with open("to_do_list/main.txt", "r", newline="") as file:
    reader = file.read()
    print(reader)