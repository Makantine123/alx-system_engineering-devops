#!/usr/bin/python3
"""
Script to export data in the JSON format
"""

import json
import requests
from sys import argv


def export_json(userID):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userID)).json()
    todos = requests.get(url + "todos", params={"userId": userID}).json()

    file_name = userID + ".json"
    data = []

    for task in todos:
        user_task = {
            "task": task["title"],
            "completed": task["completed"],
            "username": user["username"],
        }
        data.append(user_task)

    user_data = {str(user["id"]): data}

    file_name = userID + ".json"
    with open(file_name, "w") as file:
        json.dump(user_data, file)


if __name__ == "__main__":
    export_json(argv[1])
