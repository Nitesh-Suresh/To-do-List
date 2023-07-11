tasks = []

def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")

def mark_task_completed():
    view_tasks()
    task_index = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_index <= len(tasks):
        tasks[task_index-1] += " [Completed]"
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: "))
    if 1 <= task_index <= len(tasks):
        del tasks[task_index-1]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
