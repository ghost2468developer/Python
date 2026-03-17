import json
from datetime import datetime

def display_menu():
    print("Todo List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Sort Tasks by Priority")
    print("6. Sort Tasks by Due Date")
    print("7. Save Tasks")
    print("8. Quit")

def add_task(todo_list):
    task = input("Enter the task: ")
    priority = input("Enter priority (Low, Medium, High): ").capitalize()
    due_date = input("Enter due date (YYYY-MM-DD): ")
    todo_list.append({"task": task, "completed": False, "priority": priority, "due_date": due_date})
    print("Task added successfully!")

def view_tasks(todo_list):
    print("Todo List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task['task']} - Priority: {task['priority']}, Due Date: {task['due_date']}, {'Completed' if task['completed'] else 'Not Completed'}")

def mark_completed(todo_list):
    view_tasks(todo_list)
    index = int(input("Enter the number of the task to mark as completed: ")) - 1
    todo_list[index]["completed"] = True
    print("Task marked as completed!")

def delete_task(todo_list):
    view_tasks(todo_list)
    index = int(input("Enter the number of the task to delete: ")) - 1
    del todo_list[index]
    print("Task deleted successfully!")

def sort_by_priority(todo_list):
    sorted_list = sorted(todo_list, key=lambda x: x['priority'])
    view_tasks(sorted_list)

def sort_by_due_date(todo_list):
    sorted_list = sorted(todo_list, key=lambda x: datetime.strptime(x['due_date'], '%Y-%m-%d'))
    view_tasks(sorted_list)

def save_tasks(todo_list):
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)

def load_tasks():
    try:
        with open("todo_list.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    todo_list = load_tasks()
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
            sort_by_priority(todo_list)
        elif choice == '6':
            sort_by_due_date(todo_list)
        elif choice == '7':
            save_tasks(todo_list)
            print("Tasks saved successfully!")
        elif choice == '8':
            save_tasks(todo_list)
            print("Thank you for using the todo list. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
