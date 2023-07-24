#!/usr/bin/python3

import requests
import json

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"  # Replace this with the actual API URL

    # Retrieve employee information
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Retrieve TODO list for the employee
    todo_url = f"{base_url}/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print(f"Error: TODO list for Employee ID {employee_id} not found.")
        return

    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task["completed"]]
    num_done_tasks = len(done_tasks)

    # Display the progress for the current employee
    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

    return {
        employee_id: [
            {
                "username": employee_name,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todo_data
        ]
    }

def export_all_employees_todo_progress():
    all_employees_data = {}
    # Replace range with actual employee IDs or fetch from the API if available
    for employee_id in range(1, 11):
        data = get_employee_todo_progress(employee_id)
        if data:
            all_employees_data.update(data)

    file_name = "todo_all_employees.json"
    with open(file_name, "w") as file:
        json.dump(all_employees_data, file)

    print(f"Data for all employees exported to {file_name} successfully.")

if __name__ == "__main__":
    export_all_employees_todo_progress()

