#!/usr/bin/python3
"""
Script uses REST API for a given employee ID, returns information about
his/her TODO list progress
"""

import requests
from sys import argv
import csv

if __name__ == "__main__":
    userID = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users", params={"id": userID}).json()
    todos = requests.get(url + "todos", params={"userId": userID}).json()
    name = user["name"]
    completed = []

    file_name = userID + ".csv"
    with open(file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos:
            task_id = task["id"]
            task_title = task["title"]
            task_completed = str(task["completed"])
            writer.writerow([userID, name, task_completed, task_title])
