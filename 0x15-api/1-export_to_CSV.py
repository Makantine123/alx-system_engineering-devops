#!/usr/bin/python3
"""
Script uses REST API for a given employee ID, returns information about
his/her TODO list progress
"""

import requests
from sys import argv

if __name__ == "__main__":
    userID = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userID)).json()
    todos = requests.get(url + "todos", params={"userId": userID}).json()
    completed = []
    for task in todos:
        if task.get("completed") is True:
            completed.append(task.get("title"))
    print("Employee {} is done with tasks({}/{})".
          format(user.get("name"), len(completed), len(todos)))
    for title in completed:
        print("\t{}".format(title))

