# List All Users from JSONPlaceholder
# API: https://jsonplaceholder.typicode.com/users
# Goal: Display names, emails, and company names of all users.

import requests

# Get the list of all users
users = requests.get("https://jsonplaceholder.typicode.com/users").json()

# Loop through the list and print details
for user in users:
    print(f"Name: {user['name']}, Email: {user['email']}, Company: {user['company']['name']}")