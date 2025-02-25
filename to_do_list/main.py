#Connor Pavicic, to_do_list

"""What this program will do:

Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list"""

file_path = "test/main.txt" #Puts the file name in a variable instead of writing it out each time.

def add_item(): #function for adding a new item.
    """Adds a new task to the to-do list"""
    task = input('What task do you need to do?: ').strip()
    if task: #Makes sure there is a task
        with open(file_path, "a") as file:
            file.write(f"{task}: Not done yet.\n") #writes the task and makes it not done yet.
        print(f'Added task: "{task}"')

def mark_as_done(): #The function that marks something as done.
    """Marks a task as done"""
    try:
        with open(file_path, "r") as file:
            tasks = file.readlines()

        if not tasks: #Makes sure that tasks exist.
            print("No tasks found.")
            return

        print("\nCurrent tasks:") #Prints the current tasks
        for i, line in enumerate(tasks, start=1): #enumerates the tasks to make them start at 1 and not 0.
            print(f"{i}. {line.strip()}")

        task_number = int(input("\nEnter the number of the task to mark as done: ").strip()) #Has them enter a number not task name.

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = tasks[task_number - 1].replace("Not done yet.", "Done!") #Uses a 0 index now and replaces not done yet with done.

            with open(file_path, "w") as file:
                file.writelines(tasks)

            print("Task marked as done!")
        else:
            print("Invalid task number.") #Makes sure the user enters a valid task number.
    except (ValueError, FileNotFoundError): # Idiot proof to make sure the user doesn't type anything else.
        print("Error: Please enter a valid number.")

def delete_item(): #The function for deleting an item.
    """Deletes a task from the to-do list"""
    try:
        with open(file_path, "r") as file:
            tasks = file.readlines()

        if not tasks: #Makes sure there are tasks.
            print("No tasks found.")
            return

        print("\nCurrent tasks:")
        for i, line in enumerate(tasks, start=1): #Turns it to a 1 not 0 based index.
            print(f"{i}. {line.strip()}")

        task_number = int(input("\nEnter the number of the task to delete: ").strip())

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1) #Removes the task and uses the 0 based index system.

            with open(file_path, "w") as file:
                file.writelines(tasks)

            print(f'Task removed: "{removed_task.strip()}"')
        else:
            print("Invalid task number.") #All stupid proof right here.
    except (ValueError, FileNotFoundError):
        print("Error: Please enter a valid number.")

def view_tasks(): #The function to view the list.
    """Displays all tasks"""
    try:
        with open(file_path, "r") as file:
            tasks = file.readlines()

        if not tasks: #Makes sure there are tasks to print.
            print("No tasks in the list.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(tasks, start=1): #Prints each task with 1 to whatever.
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks in the list.")

# Main menu loop
def main(): #The main function
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1": #Runs each function based off what the user chose.
            add_item()
        elif choice == "2":
            mark_as_done()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1-5.")

main() #Calls function