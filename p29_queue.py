class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks

    def remove_task(self):
        if self.tasks:
            return self.tasks.pop(0)
        return ""

    def get_book(self):
        return self.tasks

    def __str__(self):
        return f"You have {len(self.tasks)} tasks."

    def __repr__(self):
        return f"TaskManager(tasks={self.tasks})"


if __name__ == '__main__':
    task_manager = TaskManager()
    print(task_manager)
    task_manager.add_task("Learn Python")
    print(task_manager)
    task_manager.add_task("Learn algorithms")
    task_manager.add_task("Learn data structures")
    print(f"All tasks: {task_manager.get_all_tasks()}")
    print(f"My actual task: {task_manager.remove_task()}")
    print(f"All tasks: {task_manager.get_all_tasks()}")
    print(f"My actual task: {task_manager.remove_task()}")
    print(f"My actual task: {task_manager.remove_task()}")
    print(f"My actual task: {task_manager.remove_task()}")
