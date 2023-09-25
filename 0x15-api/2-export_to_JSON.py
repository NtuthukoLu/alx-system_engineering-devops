#!/usr/bin/python3
"""script for parsing web data from an api
"""
import json
import requests
import sys

def fetch_user_info(user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    return json.loads(response.text)

def fetch_todo_info(user_id):
    url = f'https://jsonplaceholder.typicode.com/todos/?userId={user_id}'
    response = requests.get(url)
    return json.loads(response.text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_info = fetch_user_info(user_id)
        todo_info = fetch_todo_info(user_id)

        tasks = []

        for task in todo_info:
            task_dict = {
                'task': task['title'],
                'completed': task['completed'],
                'username': user_info['username']
            }
            tasks.append(task_dict)

        with open(f'{user_id}.json', 'w', encoding='UTF8', newline='') as f:
            json.dump(tasks, f, indent=4)

        print(f'Tasks for user {user_id} saved to {user_id}.json')
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    except KeyError:
        print(f"User with id {user_id} not found")
        sys.exit(1)

if __name__ == "__main__":
    main()

