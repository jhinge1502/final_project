from datetime import date
from Task_Class import Task
import pickle

class Tasks:
    #Defines a class which is now a collection of task objects

    def __init__(self):
        #initiates the class, looks to see if a file already exists
        self.tasks = []  # List to store Task objects
        self.file_name = ".todo.pickle"
        self.load_tasks()

    def load_tasks(self):
        #Load tasks and the unique ID counter from the pickle file
        try:
            with open(self.file_name, "rb") as f:
                data = pickle.load(f)
                # Assume data is always a dictionary
                self.tasks = data.get("tasks", [])
                Task._unique_id = data.get("id_counter", 1)
        except FileNotFoundError:
            # If the file doesn't exist, initialize a blank state
            self.tasks = []
            Task._unique_id = 1
        except Exception as e:
            print(f"Error loading tasks: {e}")


    def pickle_tasks(self):
        #Save tasks and the unique IDs to pickle file as a dict
        try:
            with open(self.file_name, "wb") as f:
                data = {"tasks": self.tasks, "id_counter": Task._unique_id}
                pickle.dump(data, f)
        except Exception as e:
            print(f"Error saving tasks: {e}")


    # Other methods (add, list, report)
    #Resources used: 
    # date.strftime() : https://www.programiz.com/python-programming/datetime/strftime
    # f string length : https://www.geeksforgeeks.org/python-padding-a-string-upto-fixed-length/



    def list(self):
        #Lists all tasks that are not complete and sorts by due date then decreasing priority as per assignment
        incomplete_tasks = [task for task in self.tasks if task.completed is None]
        incomplete_tasks.sort(key=lambda x: (x.due_date or date.max, -x.priority))
        
        print(f"{'ID':<5}{'Age':<5}{'Due Date':<12}{'Priority':<10}{'Task'}")
        print("-" * 40)
        for task in incomplete_tasks:
            age = (date.today() - task.created).days
            due_date = task.due_date.strftime("%m/%d/%Y") if task.due_date else "-"
            print(f"{task.unique_id:<5}{age:<5}{due_date:<12}{task.priority:<10}{task.name}")

    def report(self):
        #Report of all tasks complete and incomplete taks
        print(f"{'ID':<5}{'Age':<5}{'Due Date':<12}{'Priority':<10}{'Task':<20}{'Created':<30}{'Completed'}")
        print("-" * 100)
        for task in self.tasks:
            age = (date.today() - task.created).days
            due_date = task.due_date.strftime("%m/%d/%Y") if task.due_date else "-"
            created = task.created.strftime("%c")
            completed = task.completed.strftime("%c") if task.completed else "-"
            print(f"{task.unique_id:<5}{age:<5}{due_date:<12}{task.priority:<10}{task.name:<20}{created:<30}{completed}")

    def done(self, unique_id):
        #Marks a task as completed based on unique id provided
        for task in self.tasks:
            if task.unique_id == unique_id:
                task.mark_as_completed()
                self.pickle_tasks()
                print(f"Completed task {unique_id}")
                return
        print(f"Task with ID {unique_id} not found.")

    def delete(self, unique_id):
        #Deletes a task
        self.tasks = [task for task in self.tasks if task.unique_id != unique_id]
        self.pickle_tasks()
        print(f"Deleted task {unique_id}")

    def query(self, terms):
        #Searchs to word match with task names
        results = [
            task for task in self.tasks
            if task.completed is None and any(term.lower() in task.name.lower() for term in terms)
        ]
        results.sort(key=lambda x: (x.due_date or date.max, -x.priority))
        
        print(f"{'ID':<5}{'Age':<5}{'Due Date':<12}{'Priority':<10}{'Task'}")
        print("-" * 40)
        for task in results:
            age = (date.today() - task.created).days
            due_date = task.due_date.strftime("%m/%d/%Y") if task.due_date else "-"
            print(f"{task.unique_id:<5}{age:<5}{due_date:<12}{task.priority:<10}{task.name}")

    def add(self, name, priority=1, due_date=None):
        #Adds a new task
        try:
            task = Task(name=name, priority=priority, due_date=due_date)
            self.tasks.append(task)
            self.pickle_tasks()
            print(f"Created task {task.unique_id}")
        except Exception as e:
            print(f"Error adding task: {e}")
