import argparse
import pickle
from datetime import datetime
from datetime import date
from Tasks_Class import Tasks
from Task_Class import Task

###################################################################
#Creates a helper fct to use in main to ensure dates are correct format
def parse_date(date_str):
    """Helper function to parse dates from the command line."""
    try:
        return datetime.strptime(date_str, "%m/%d/%Y").date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_str}. Use MM/DD/YYYY.")

def main():
    #Initialize the task manager
    tasks_manager = Tasks()

    #Create an argument parser
    parser = argparse.ArgumentParser(description="Update yuour ToDo List")
    
    #Adding arguments based on key words as provided in the assignment
    '''
    #Assignment states: The user should run the program completely from the command line passing in commands and arguments 
    that will alter the behavior of the program. The commands are --add, --delete, --list, --report, --query, and --done. 
    Use the argparse package to help with parsing the command line arguements
    '''
    parser.add_argument("--add", type=str, help="Add a new task", required = False)
    parser.add_argument("--priority", type=int, choices=[1, 2, 3], help="Priority of the task", default=1, required = False)
    parser.add_argument("--due", type=parse_date, help="Duedate in MM/DD/YYYY format", required = False)

    parser.add_argument("--list", action="store_true", help="Lists all incomplete tasks")
    parser.add_argument("--report", action="store_true", help="Report of all tasks complete and incomplete taks")

    parser.add_argument("--done", type=int, help="Marks a task as completed based on unique id provided")
    parser.add_argument("--delete", type=int, help="deletes a task from report based on unique id provided")
    parser.add_argument("--query", nargs="+", help="Searchs to word match with task names")

    #Parse arguments
    args = parser.parse_args()

    #execute commands based on input from user in command line
    if args.add:
        tasks_manager.add(name=args.add, priority=args.priority, due_date=args.due)
    elif args.list:
        tasks_manager.list()
    elif args.report:
        tasks_manager.report()
    elif args.done:
        tasks_manager.done(unique_id=args.done)
    elif args.delete:
        tasks_manager.delete(unique_id=args.delete)
    elif args.query:
        tasks_manager.query(terms=args.query)

if __name__ == "__main__":
    main()
