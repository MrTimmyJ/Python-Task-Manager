tasks = []

def add_task():
    task = input("Enter task description: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def mark_task_complete():
    if not tasks:
        print("No tasks available to mark as complete.")
        return
    view_tasks()
    task_index = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['task']}' marked as complete!")
    else:
        print("Invalid task number.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        i = 1
        for task in tasks:
            if task["completed"]:
                status = "Completed"
            else:
                status = "Incomplete"
            
            print(f"{i}. {task['task']} - {status}")
            i += 1

def delete_task():
    if not tasks:
        print("No tasks available to delete.")
        return
    view_tasks()
    task_index = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task['task']}' deleted successfully!")
    else:
        print("Invalid task number.")

def filter_tasks():
    print("Filter by: \n1. Completed tasks\n2. Incomplete tasks")
    filter_option = input("Enter your choice: ")

    if filter_option == "1":
        filtered_tasks = []
        for task in tasks:
            if task["completed"]:
                filtered_tasks.append(task)
    elif filter_option == "2":
        filtered_tasks = []
        for task in tasks:
            if not task["completed"]:
                filtered_tasks.append(task)
    else:
        print("Invalid option.")
        return

    if filtered_tasks:
        print("\nTasks:")
        i = 1
        for task in filtered_tasks:
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{i}. {task['task']} - {status}")
            i += 1
    else:
        if filter_option == "1":
            print("No completed tasks found.")
        elif filter_option == "2":
            print("No incomplete tasks found.")

def show_menu():
    print(
        "\nWelcome to the Task Manager Application!\n"
        "1. Add Task\n"
        "2. Mark Task as Complete\n"
        "3. View Tasks\n"
        "4. Delete Task\n"
        "5. Filter Tasks\n"
        "6. Exit"
    )

while True:
    show_menu()
    choice = input("Please enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        mark_task_complete()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        filter_tasks()
    elif choice == "6":
        print("Exiting Task Manager")
        break
    else:
        print("Invalid choice. Please try again.")