import json
import os
from datetime import datetime
import time
from tkinter import messagebox
import tkinter as tk
tk().withdraw()
def add_tasks():
    task_name=input("enter the task:")
    while True:
        task_time=input("enter the time in HH:MM format :")
        try:
            datetime.strptime(task_time,"%H:%M")
            break
        except ValueError:
            print("invalid time format")
    if not os.path.exists("taskrem.json"):
        task={"tasks":[]}
    else:
        with open("taskrem.json","r")as file:
            task=json.load(file)
    task["tasks"].append({"task":task_name,"time":task_time,"notified":False})
    with open("taskrem.json","w")as file:
        json.dump(task,file,indent=4)
        print("task added sucessfully")
def auto_reminder():
    try:
        if not os.path.exists("taskrem.json"):
            task={"tasks":[]}
        else:
            with open("taskrem.json","r")as file:
                task=json.load(file) #you need to load json file into a variable
    except json.JSONDecodeError:
        task={"tasks":[]}
    while True:
        now=datetime.now().strftime("%H:%M")
    
        for t in task['tasks']:
            if not t["notified"] and t["time"]==now:
                messagebox.showinfo(title="taskreminder",message=f"reminder: {t['task']}")
                t["notified"]=True
        with open("taskrem.json","w")as file:
            json.dump(task,file,indent=4)
        time.sleep(60)
choice=input("enter your choice: 1.add task,2.exists")
while True:
    if(choice=="1"):
        add_tasks()
    elif(choice=="2"):
        break
    else:
        print("invalid")
auto_reminder()
#i will update this in future this code is a   garbage will add ne function bored and so lazy so i drop it
#Delete Task by Name or Time
#Allow users to remove tasks from the JSON.

#View Upcoming Tasks
#Print the tasks sorted by time.

#Edit Task Time or Name
#Useful if you entered the wrong time.

#Mark Task as Done (like a checkbox)
#Visually show completed tasks with a ✔️.

#GUI with Tkinter
#If you want to upgrade from CLI to graphical view.

#System Tray Popup (Advanced)
#Instead of messagebox, send real system notifications using plyer.


