# Connor Pavicic, to_do_list

"""What this program will do:

Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list"""

with open("to_do_list/main.txt", "w", newline="") as file:
    file.write("")

def add_item():
    with open("to_do_list/main.txt", "a", newline="") as file:
        task = input('What task do you need to do?: ')
        to_be_appended = task + ": Not done yet."
        file.write(f"\n{to_be_appended}")

add_item()

with open("to_do_list/main.txt", "r", newline="") as file:
    contents = file.read()
    print(contents)

def mark_as_done():
    with open("to_do_list/main.txt", "a+", newline="") as file:
        to_be_marked = input('Which task do you want to replace?: ').lower().strip()
        task_list = file.read()
        marked_list = []
        for item in task_list:
            if to_be_marked in item:
                marked_list.append(item)

        if len(marked_list) == 0:
            print(f'{to_be_marked} not found.')
        elif len(marked_list) == 1:
            r_u_sure = input(f'Are you sure you want to mark {marked_list} as done? (y or n): ').lower().strip()
            if r_u_sure == 'y':
                item = marked_list
            elif r_u_sure == 'n':
                print('Ok')
            else:
                print('Incorrect option. I will assume you are saying no.')

mark_as_done()
       

with open("to_do_list/main.txt", "r", newline="") as file:
    contents = file.read()
    print(contents)