def show_menu():
    print("\n1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Prioritize Task")
    print("7. Add Deadline to Task")
    print("8. Exit")

def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def list_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("\nNo tasks available.")
            return
        print("\nPending Tasks:")
        for index, task in enumerate(tasks):
            if "[Completed]" not in task:
                print(f"{index + 1}. {task.strip()}")
        print("\nCompleted Tasks:")
        for index, task in enumerate(tasks):
            if "[Completed]" in task:
                print(f"{index + 1}. {task.strip()}")
    except FileNotFoundError:
        print("\nNo tasks available.")

def mark_task_completed():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1] = tasks[task_number - 1].strip() + " [Completed]\n"
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def edit_task():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to edit: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_number - 1] = new_task + "\n"
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task edited!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def prioritize_task():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to prioritize: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            task = tasks.pop(task_number - 1).strip()
            tasks.insert(0, task + " [Priority]\n")
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task prioritized!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_deadline():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to add a deadline: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            deadline = input("Enter the deadline (YYYY-MM-DD): ")
            tasks[task_number - 1] = tasks[task_number - 1].strip() + f" [Deadline: {deadline}]\n"
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Deadline added!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            edit_task()
        elif choice == '6':
            prioritize_task()
        elif choice == '7':
            add_deadline()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
