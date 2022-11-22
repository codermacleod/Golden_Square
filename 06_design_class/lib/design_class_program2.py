class TaskCompleter():
    def __init__(self):
        self.task_list = []

    def complete_task(self,task):
        self.task_list.remove(task)
        

    def add_task(self,task=None):
        if task == None:
            return "You haven't added a task..."
        elif type(task) == int:
            return "Please enter a string"
        else:
            self.task_list.append(task)
            return task

    def list_task(self):
        listed_tasks = ", ".join(self.task_list)
        return listed_tasks


