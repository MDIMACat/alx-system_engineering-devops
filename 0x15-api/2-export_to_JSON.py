#!/usr/bin/python3
"""
Script to retieve data from an API and write to JSON
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    TODOS_url = f"{base_url}/users/{employee_id}/todos"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    todo_response = requests.get(TODOS_url)
    todo_data = todo_response.json()
    emp_id = employee_data['id']
    emp_usr = employee_data['username']
    json_file_name = f"{emp_id}.json"

    tasks_list = []
    for task in todo_data:
        tsk_T = task['title']
        tsk_comp = task['completed']
        task_data = {"task": tsk_T, "completed": tsk_comp, "username": emp_usr}
        tasks_list.append(task_data)

    user_data = {emp_id: tasks_list}

    with open(json_file_name, 'w') as json_file:
        json.dump(user_data, json_file)
