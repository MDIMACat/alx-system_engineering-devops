#!/usr/bin/python3
"""
Script to retieve data from an API
"""

import requests
from sys import argv
import csv

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
    emp_username = employee_data['username']

    csv_file_name = f"{emp_id}.csv"

    with open(csv_file_name, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            task_completed = task['completed']
            task_title = task['title']
            writer.writerow([emp_id, emp_username, task_completed, task_title])
