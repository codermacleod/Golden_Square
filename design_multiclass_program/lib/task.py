class Task():
    def __init__(self,task):
        self.task = task
        self.incomplete = True
        
    def set_as_complete(self):
        self.incomplete=False
    