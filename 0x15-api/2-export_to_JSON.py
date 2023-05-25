#!/usr/bin/python3
"""
Script to export data in the JSON format
"""

import csv
import json
import requests
from sys import argv


def export_csv(userID):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userID)).json()
    todos = requests.get(url + "todos", params={"userId": userID}).json()
    name = user.get("username")

    file_name = userID + ".json"

    user_data = {userID: []}

    for task in todos:
        user_task = {
            "task": task["title"],
            "completed": task["completed"],
            "username": name,
        }
        user_data[userID].append(user_task)

    jdata = json.dumps(user_data)

    file_name = userID + ".json"
    with open(file_name, "w") as json_file:
        json_file.write(jdata)


if __name__ == "__main__":
    export_csv(argv[1])
