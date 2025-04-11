class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str):
        if not task:
            raise ValueError("Task cannot be empty.")
        self.tasks.append(task)

    def remove_task(self, task: str):
        if task not in self.tasks:
            raise ValueError(f"Task '{task}' not found.")
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks.copy()

    def clear_tasks(self):
        self.tasks.clear()
