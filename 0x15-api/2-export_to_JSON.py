#!/usr/bin/python3
"""
Script to export data in the JSON format
"""

import json
import requests
from sys import argv


def export_json(userID):
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get(url + "todos", params={"userId": userID}).json()
    user = requests.get(url + "users/{}".format(userID)).json()
    file_name = userID + ".json"

    file_name = userID + ".json"
    with open(file_name, "w") as file:
        for t in todos:
            json.dump({userID: [{"task": t["title"],
                                 "completed": t["completed"],
                                 "username": user["username"]}]}, file)


if __name__ == "__main__":
    export_json(argv[1])
