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
        file.write(f"\n {to_be_appended}")

def replace():
    with open("to_do_list/main.txt", "r+") as file:
        main_txt = file.readlines()
        to_be_replaced = input('What text do you want to replace?: ')
        to_be_replaced_with = input(f'What do you want to replace {to_be_replaced} with?: ')

        n = 0
        for i in main_txt:
            if to_be_replaced in i:
                confirm = input(f'Are you sure you want to replace {i} with {to_be_replaced_with}? (yes or no): ').lower().strip()
                if confirm == 'yes':
                    replacement = i.replace(to_be_replaced, to_be_replaced_with)

                    main_txt[n] = replacement
                elif confirm == 'no':
                    break
                else:
                    print('Incorrect option, exiting the replace feature.')
                    break
            n += 1

replace()

    

with open("to_do_list/main.txt", "r", newline="") as file:
    contents = file.read()

print(contents)