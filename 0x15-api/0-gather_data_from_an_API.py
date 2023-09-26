#!/usr/bin/python3
"""using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    todo_url = url + "/user/{}/todos".format(argv[1])
    name_url = url + "/users/{}".format(argv[1])
    all_todo = get(todo_url).json()
    emp_name = get(name_url).json()
    no_of_todo = len(all_todo)
    finished_todo = len([all_todos for completes in all_todo
        if completes.get("completed")])
    emp_names = emp_name.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(emp_names, finished_todo, all_todo))
    for todo in all_todo:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
