class TaskList():
    def __init__(self):
        self.tasklist=[]
        
    def add_task(self,task):
        # add todo item to the list
        self.tasklist.append(task)

    def complete(self):
        #return list when task.incomplete == False
        comp_tasks=[]
        for task in self.tasklist:
            if task.incomplete == False:
                comp_tasks.append(task.task)
                self.tasklist.remove(task)
        return comp_tasks

    def incomplete(self):
        return [task.task for task in self.tasklist]