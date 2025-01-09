from task import Task
from datetime import datetime


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            status = "X" if task.completed else " "
            print(f"[{status}] ID {task.task_id}: {task.description} (Due: {task.due_date})")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.set_completed()

    def remove_all_tasks(self):
        self.tasks = []

    def update_task(self, task_id, updated_description, updated_due_date):
        for task in self.tasks:
            if task.task_id == task_id:
                task.description = updated_description
                task.due_date = updated_due_date

    def display_pending_tasks(self):
        print("\n--- Pending Tasks ---")
        pending = [task for task in self.tasks if not task.completed]
        if not pending:
            print("No pending tasks available.")
        else:
            for task in pending:
                print(f"[ ] ID {task.task_id}: {task.description} (Due: {task.due_date})")

    def organize_tasks_by_date(self):
        self.tasks = sorted(self.tasks, key=lambda task: task.due_date)


if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\n=== Task Management System ===")
        print("1. Create a new task")
        print("2. Show all tasks")
        print("3. Mark a task as completed")
        print("4. Remove all tasks")
        print("5. Update a task")
        print("6. Show pending tasks")
        print("7. Organize tasks by due date")
        print("8. Exit")

        option = input("Select an option: ")

        if option == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d")
                new_task = Task(len(manager.tasks) + 1, description, due_date)
                manager.create_task(new_task)
                print("Task successfully created!")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

        elif option == "2":
            print("\n--- Task List ---")
            manager.display_tasks()

        elif option == "3":
            task_id = int(input("Enter the ID of the task to complete: "))
            manager.complete_task(task_id)
            print("Task marked as completed!")

        elif option == "4":
            manager.remove_all_tasks()
            print("All tasks have been removed.")

        elif option == "5":
            task_id = int(input("Enter the ID of the task to update: "))
            updated_description = input("Enter the new description: ")
            updated_due_date = input("Enter the new due date (YYYY-MM-DD): ")
            try:
                updated_due_date = datetime.strptime(updated_due_date, "%Y-%m-%d")
                manager.update_task(task_id, updated_description, updated_due_date)
                print("Task updated successfully!")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

        elif option == "6":
            manager.display_pending_tasks()

        elif option == "7":
            manager.organize_tasks_by_date()
            print("Tasks have been organized by due date.")
            manager.display_tasks()

        elif option == "8":
            print("Exiting the Task Management System.")
            break

        else:
            print("Invalid option. Please try again.")
