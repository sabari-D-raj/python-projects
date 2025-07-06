import json
import os
def addtask():
    text=input("enter the task: ")
    if  os.path.exists("task.json"):   # Check if the file exists
        # If it exists, read the existing tasks
         with open("task.json","r")as file:
            try:
                tasks= json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else: # If it does not exist, create an empty list for tasks
        tasks = []
    tasks.append({"task":text,"compeleted":False}) # Append the new task to the list
    # Write the updated tasks back to the file
    with open("task.json","w") as file:
        json.dump(tasks,file, indent=4)  #indent=4 for pretty printing and readability
    print("Task added successfully.")

def marktask():
    if os.path.exists("task.json"):
        with open("task.json","r")as file:
            try:
                tasks=json.load(file)
            except json.JSONDecodeError:
                tasks = []
        viewtasks()
        tasknumber=int(input("enter the task number to mark as completed"))
        if 0 < tasknumber <=len(tasks):
            tasks[tasknumber-1]["compeleted"]=True          
            with open("task.json","w")as file:
                json.dump(tasks,file, indent=4)
            print("Task marked as completed.")
      
def deletetask():
    if os.path.exists("task,json"):
        with open("task.json","r")as file:
            try:
                tasks=json.load(file)
            except json.JSONDecodeError:
                tasks = []
        viewtasks()
        tasknumber=int(input("enter ther task numeber to delete: "))
        if 0< tasknumber <=len(tasks):
            tasks.pop(tasknumber-1) # Remove the task from the list
            with open("task.json","w")as file:
                json.dump(tasks,file,indent=4)
            print("Task deleted successfully.")
def viewtasks():
    if os.path.exists("task.json"):
        with open("task.json","r")as file:
            try:
                tasks=json.load(file)
            except json.JSONDecodeError:  #It’s an error raised when Python tries to read (decode) a JSON file that is:
                tasks = []                       # not properly formatted or is empty.  Contains invalid syntax  
            if not tasks:
                print("tasks is not found")
            else:
                for i, task in  enumerate(tasks,start=1): #create a note about enumerate at last
                    status="✔️" if task["compeleted"] else "❌"
                    print(f"{i} : {task["task"]} : {status}")
    else:
        print("No tasks found. Please add a task first.")
while True:
    command=input("enter a command (1:add,2:mark,3:delete,4:view,5:exit)")
    if command=="1":
        addtask()
    elif command=="2":
        marktask()
    elif command=="3":
        deletetask()
    elif command=="4":
        viewtasks()
    elif command=="5":
        print("bye...byee 💋")
        break
    else:
        print("Invalid command. Please try again.")
# Note: The code above is a simple task management system that allows users to add, mark, delete, and view tasks stored in a JSON file.
# It uses the `json` module to read and write tasks to a file named `task.json`. The tasks are stored as a list of dictionaries, where each dictionary represents a task with its description and completion status. The program runs in a loop, allowing users to perform various operations until they choose to exit.
# The code also includes error handling for JSON decoding errors, ensuring that the program can handle cases where the JSON file is empty or improperly formatted.
# The tasks are displayed with their status, using checkmarks for completed tasks and cross marks for  incomplete tasks. The user can interact with the program through a command-line interface, making it easy to manage tasks.   
#--------------enumerate-------------------
# enumerate() is function that adds a counter index to an iterable like list,tuple ,or string
# # It returns an enumerate object that contains pairs of index and value.
# # This is useful when you need to keep track of the index while iterating over a COLLECTION
# syantax:
# enumerate(iterable, start=0) start is optional and specifies the starting index (default is 0).
# # Example:
# fruits = ["apple", "banana", "cherry"]
# for i,fruit in enumerate(fruits, start=1):
#     print(f"{i}: {fruit}")
# # Output:
# 1: apple    # This will start the index from 1 instead of 0
# 2: banana
# 3: cherry          