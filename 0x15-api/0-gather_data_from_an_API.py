#!/usr/bin/python3
"""Runs the REST API"""
import urllib.request
import json
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/todos"

    """Fetching employee data"""
    employee_url = f"{base_url}?userId={employee_id}"
    with urllib.request.urlopen(employee_url) as response:
        employee_data = json.load(response)

    """calculating progress"""
    total_tasks = len(employee_data)
    completed_tasks = sum(task['completed'] for task in employee_data)

    """Displaying progress"""
    print(f"Employee {employee_data[0]['userId']} is done with tasks\
            ({completed_tasks}/{total_tasks}):")
    print(f"{employee_data[0]['userId']}: {employee_data[0]['title']}")

    """Displaying completed tasks"""
    for task in employee_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
