# Task 4: POST Request (Sending Data)
# Instructions:
# 1.	Use the same API to create a new post.
# 2.	Send a JSON payload with:
# {
#   "title": "New Post",
#   "body": "This is a test post.",
#   "userId": 1
# }
# 3.	Print the response (should include the new post with an ID).
# Expected Output:
# New Post: {'title': 'New Post', 'body': 'This is a test post.', 'userId': 1, 'id': 101}

import requests

api = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api)

# JSON payload to send
payload = {
    "title": "New Post",
    "body": "This is a test post.",
    "userId": 1
}

# Send POST request
response = requests.post(api, json=payload)

# Convert response to JSON
new_post = response.json()

# Print the response
print(f"New Post: {new_post}")