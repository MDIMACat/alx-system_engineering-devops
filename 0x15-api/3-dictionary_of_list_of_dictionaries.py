#!/usr/bin/python3
"""
Script to retrieve data from an API and write to JSON
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    all_employees_data = {}

    for employee_id in argv[1:]:
        employee_url = f"{base_url}/users/{employee_id}"
        todos_url = f"{base_url}/users/{employee_id}/todos"
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        todo_response = requests.get(todos_url)
        todo_data = todo_response.json()

        emp_id = employee_data['id']
        emp_usr = employee_data['username']

        tasks_list = []
        for todo in todo_data:
            task_data = {"username": emp_usr, "task": todo.get("title"),
                         "completed": todo.get("completed")}
            tasks_list.append(task_data)

        all_employees_data[emp_id] = tasks_list

    json_file_name = "todo_all_employees.json"

    with open(json_file_name, 'w', encoding="utf-8") as json_file:
        json.dump(all_employees_data, json_file)
