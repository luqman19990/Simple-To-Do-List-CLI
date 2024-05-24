def show_menu():
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def list_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task.strip()}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
