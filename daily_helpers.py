# daily_helpers.py

import datetime

# 1. Reminder function
def set_reminder(task, time):
    
    now = datetime.datetime.now()
    reminder_time = datetime.datetime.strptime(time, "%H:%M").replace(
        year=now.year, month=now.month, day=now.day
    )
    if reminder_time < now:
        return 
    return f"Reminder set for '{task}' at {time}."

# 2. Temperature conversion
def celsius_to_fahrenheit(celsius):
    
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    
    return (fahrenheit - 32) * 5/9

# 3. Simple to-do list
to_do_list = []

def add_task(task):
    
    to_do_list.append(task)
    return f"Task added: {task}"

def view_tasks():
   
    if not to_do_list:
        return 
    return "\n".join([f"{i+1}. {task}" for i, task in enumerate(to_do_list)])

def clear_tasks():
    
    to_do_list.clear()
    return "To-do list cleared!"
