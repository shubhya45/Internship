# Part 2: Making API Requests with Python
# Task 3: GET Request (Fetching Data)
# Use the JSONPlaceholder API (a free fake API for testing):
# •	Endpoint: https://jsonplaceholder.typicode.com/posts
# Instructions:
# 1.	Write a Python script to fetch all posts from the API.
# 2.	Print the response status code.
# 3.	Print the first post in the response (JSON format).


# Expected Output:
# Status Code: 200  
# First Post: {'userId': 1, 'id': 1, 'title': '...', 'body': '...'}

import requests

api = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api)

# Fix: Call the .json() method to get the actual JSON data
po = response.json()

# Fix: Use correct casing: status_code, not Status_code
print(f"All posts:\n{po}")
print(f"Status code:\n{response.status_code}")

# Fix: Define and print the first post properly
first_post = po[0]  # po is a list of posts
print(f"First post:\n{first_post}")