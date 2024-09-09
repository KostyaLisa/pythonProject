# The project consists of creating a task list system where the user can add tasks, set priorities, mark tasks as completed, remove completed tasks, and display all pending tasks with their respective priorities.
# Features:
#
# Main Menu with options:
# - Add Task
# - Show Tasks
# - Mark Task as Complete
# - Remove Completed Tasks
# - To go out
#
# Add Task: User can add a task by providing description and priority (e.g. High, Medium, Low).
# This information is stored in a list of dictionaries.
#
# Show Tasks:
# View a list of all pending tasks, showing description and priority.
# Tasks can be displayed in order of priority or registration.
#
# Mark Task as Complete: Allow the user to mark a task as complete, removing it from the to-do list or moving it to a list of completed tasks.
#
# Remove Completed Tasks: Remove all tasks that have been marked as completed from the list.
#
# Exit: End the program.
#
# Technical Requirements:Use of Lists: The list must be used to store all tasks.
# Use of Dictionaries: Each task must be represented by a dictionary with the keys description, priority and completed.
#
# Tips:Start with the main menu and implement the basic functionalities.
# Think about how to use a dictionary to represent each task and how to store that in a list.
# When marking a task as complete, consider changing the value of a completed key to True.
# Implement the functionality to remove completed tasks so that it only deletes those that are marked as completed.
#
# Additional Challenge (Optional):
# - Add a functionality to edit the description or priority of a task.
# - Allow the user to sort tasks by priority or registration date before displaying.


# Example implementation:

tasks = []

def add_task():
    description = input("Enter task description: ")
    priority = input("Enter task priority (High, Medium, Low): ")
    completed = False
    tasks.append({"description": description, "priority": priority, "completed": completed})
    print("Task added successfully!")
    main_menu()


def show_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("Task List:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. Description: {task['description']}, Priority: {task['priority']}, Completed: {task['completed']}")

    main_menu()


def mark_task_complete():
    if len(tasks) == 0:
        print("No tasks found.")
        return

    task_number = int(input("Enter the number of the task to mark as complete: "))
    if task_number <= 0 or task_number > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[task_number-1]
    if task["completed"]:
        print("Task is already marked as complete.")
    else:
        task["completed"] = True
        print("Task marked as complete successfully!")

    main_menu()


def remove_completed_tasks():
    completed_tasks = [task for task in tasks if task["completed"]]
    tasks[:] = [task for task in tasks if not task["completed"]]

    print(f"Removed {len(completed_tasks)} completed tasks.")
    main_menu()


def exit_program():
    print("Exiting the program...")
    exit()


def main_menu():
    print("\nMain Menu:")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Complete")
    print("4. Remove Completed Tasks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        show_tasks()
    elif choice == 3:
        mark_task_complete()
    elif choice == 4:
        remove_completed_tasks()
    elif choice == 5:
        exit_program()
    else:
        print("Invalid choice. Please try again.")
        main_menu()



main_menu()

