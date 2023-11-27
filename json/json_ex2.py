import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

print(todos[:2])

todos_by_user = {}
"""
Let's count how many todos are completed for each user.
"""
for todo in todos:
    if todo["completed"]: # We don't need the == true, its binary and python knows that
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]] = 1

"""
Now let's use a set comprehension to find out the set of people who completed the most todos:
"""

top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

max_complete = top_users[0][1]

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

print(f"user(s) {max_users} completed {max_complete} TODOs")