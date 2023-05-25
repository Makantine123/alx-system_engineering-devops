#!/usr/bin/python3
"""
Script uses REST API for a given employee ID, returns information about
his/her TODO list progress
"""

import csv
import requests
from sys import argv


def export_csv(userID):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userID)).json()
    todos = requests.get(url + "todos", params={"userId": userID}).json()
    name = user.get("username")

    file_name = userID + ".csv"
    with open(file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])
        for task in todos:
            task_title = task.get("title")
            task_completed = str(task.get("completed"))
            writer.writerow([userID, name, task_completed, task_title])


if __name__ == "__main__":
    export_csv(argv[1])
