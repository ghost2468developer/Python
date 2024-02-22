# Function to display the main menu
def display_menu():
    print("Todo List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Quit")

# Function to add a task to the todo list
def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to view all tasks in the todo list
def view_tasks(todo_list):
    print("Todo List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task['task']} - {'Completed' if task['completed'] else 'Not Completed'}")

# Function to mark a task as completed
def mark_completed(todo_list):
    view_tasks(todo_list)
    index = int(input("Enter the number of the task to mark as completed: ")) - 1
    todo_list[index]["completed"] = True
    print("Task marked as completed!")

# Function to delete a task from the todo list
def delete_task(todo_list):
    view_tasks(todo_list)
    index = int(input("Enter the number of the task to delete: ")) - 1
    del todo_list[index]
    print("Task deleted successfully!")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("Thank you for using the todo list. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
