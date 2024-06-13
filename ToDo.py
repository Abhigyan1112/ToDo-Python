import tkinter as UI
import requests
import json
category = 'inspirational'
quote=''
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': 'knOUuLi9nJWgllPOJsNirw==kJ1cUK6UEwWqkguF'})
if response.status_code == 200:
    quote=response.json()
    quote=quote[0]['quote']
else:
    print("Error:", response.status_code, response.text)

tasks_file="tasks.json"
tasks=[]

def download_tasks():
    prev_tasks=[]
    try:
        with open(tasks_file,'r') as file:
            prev_tasks=json.load(file)
    except Exception:
        return []
    return prev_tasks

tasks=download_tasks()

def upload_tasks():
    with open(tasks_file,'w') as file:
        json.dump(tasks,file)

window=UI.Tk()
window.title("Your daily To-do. Have a great day")
window.geometry("700x700")

quote_line=UI.Label(window, text='"'+quote.upper()+'"', font=("Comic Sans MS", 12, "bold"), wraplength=700)
quote_line.pack()

task_list = UI.Listbox(window, width=76)
task_list.pack()

def display_prev_tasks():
    for t in tasks:
        task_list.insert(UI.END,t)
        
display_prev_tasks()
    
new_task_entry = UI.Entry(window, width=50)
new_task_entry.pack()  # Add the entry widget to the window

def add_task():
    task = new_task_entry.get()
    if task != "":
        task_list.insert(UI.END, task)
        new_task_entry.delete(0, UI.END)  # Clear the entry field
        tasks.append(task)
        upload_tasks()

add_task_button = UI.Button(window, text="Add Task", command=add_task)
add_task_button.pack()  # Add the button to the window

def delete_task():
    selected_item = task_list.curselection()
    if selected_item:
        selected_task=[task_list.get(index) for index in selected_item]
        tasks.remove(selected_task[0])
        task_list.delete(selected_item[0])
        upload_tasks()
    

delete_task_button = UI.Button(window, text="Delete Task", command=delete_task)
delete_task_button.pack()  # Add the button to the window

window.mainloop()

