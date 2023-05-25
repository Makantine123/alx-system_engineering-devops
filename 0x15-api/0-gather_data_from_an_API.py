#!/usr/bin/python3
"""
Script uses REST API for a given employee ID, returns information about
his/her TODO list progress
"""


import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com/"


def check_task(userID):
    user = requests.get(url + "users/{}".format(userID)).json()
    todos = requests.get(url + "todos", params={"userId": userID}).json()
    name = user.get("name")
    completed = []
    for task in todos:
        if task.get("completed") is True:
            completed.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".
          format(name, len(completed), len(todos)))
    for title in completed:
        print("\t{}".format(title))


if __name__ == "__main__":
    check_task(int(argv[1]))
