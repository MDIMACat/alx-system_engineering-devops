#!/usr/bin/python3
"""
Script to retieve data from an API
"""

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

    total_task = len(todo_data)
    emp_name = employee_data['name']
    comp_task = 0
    for task in todo_data:
        if task['completed'] is True:
            comp_task += 1

    print(f'Employee {emp_name} is done with tasks({comp_task}/{total_task}):')
    for task in todo_data:
        if task['completed'] is True:
            print(f"\t{task['title']}")
