
import json
from pathlib import Path

# File where tasks will be saved
file_name = Path("tasks.json")


def load_tasks():
    if file_name.exists():
        with open(file_name, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    name = input("Enter your task: ")

    if name.strip():
        tasks.append({
            "name": name,
            "completed": False
        })
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task name cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("You have no tasks yet.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['name']} - {status}")


def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter the task number completed: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n=== MY PRODUCTIVITY TOOL ===")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Complete a task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("Goodbye! Stay productive.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
