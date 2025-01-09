class Task:
    def __init__(self, task_id, description, due_date, completed=False):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def set_completed(self):
        self.completed = True
