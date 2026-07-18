# Project 04 - To-Do List that saves to file
FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []  # if file doesn't exist yet, start empty

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

print("--- Your To-Do List ---")

while True:
    print("\n1. View Tasks  2. Add Task  3. Delete Task  4. Exit")
    choice = input("Choose (1-4): ")

    if choice == '1':
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Added: '{new_task}'")

    elif choice == '3':
        if not tasks:
            print("Nothing to delete!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num-1)
                save_tasks(tasks)
                print(f"Deleted: {removed}")
            except:
                print("Invalid number!")

    elif choice == '4':
        print("Bye! Your tasks are saved in tasks.txt")
        break
    else:
        print("Invalid choice")