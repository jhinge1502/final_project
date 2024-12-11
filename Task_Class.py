import pickle
from datetime import date


class Task:
    """Representation of a task
  
             Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
    """
    
    _unique_id = 1 #This will create an keep a track of the unique IDs that are required for each task
    def __init__(self, name, priority=1, due_date=None):
        
        #All attributes are defined
        self.created = date.today()
        self.completed = None
        self.name = name
        self.unique_id = Task._unique_id
        Task._unique_id += 1
        self.priority = priority
        self.due_date = due_date

        

    def mark_as_completed(self):
        #Marks the task as completed by setting the completed date
        self.completed = date.today()

    def __str__(self):
        #Defines that it means to print a task
        status = "Completed" if self.completed else "Pending"
        due = f", Due: {self.due_date}" if self.due_date else ""
        return (f"[{status}] Task ID: {self.unique_id}, Name: {self.name}, "
                f"Priority: {self.priority}{due}, Created: {self.created}, "
                f"Completed: {self.completed}")