#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"  # Replace this with the actual API URL

    # Retrieve employee information
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Error: Employee not found.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Retrieve TODO list for the employee
    todo_url = f"{base_url}/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print("Error: TODO list not found.")
        return

    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task["completed"]]
    num_done_tasks = len(done_tasks)

    # Display the progress
    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

