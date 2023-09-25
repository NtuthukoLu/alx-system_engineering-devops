#!/usr/bin/python3
"""
Script that exports information about an employees TODO list progress
given an employee id to a CSV file named `USER_ID.csv`.
"""
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    user_response = requests.get(url)
    user_info = json.loads(user_response.text)

    builder = {}
    for user in users:
        employee_id = user.get('id')
        user_id_key = str(employee_id)
        username = user.get('username')
        builder[user_id_key] = []
        url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\.format(employee_id)

        response = requests.get(url)
        objs = json.loads(response.text)
        for obj in objs:
                json_data = {
                    "task": obj.get('title'),
                    "completed": obj.get('completed'),
                    "username": username
                }
                builder[user_id_key].append(json_data)

    # write the data to the file
    json_encoded_data = json.dumps(builder)
    with open('todo_all_employees.json', 'w') as myFile:
        myFile.write(json_encoded_data)
