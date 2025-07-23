# Task 5: Error Handling & Authentication
# Instructions:
# 1.	Try accessing a non-existent endpoint (e.g., https://jsonplaceholder.typicode.com/nonexistent).
# 2.	Handle the error (check status code, print an error message if request fails).
# Example Code:
# response = requests.get("https://jsonplaceholder.typicode.com/nonexistent")

import requests

# Attempt to access a non-existent endpoint
url = "https://jsonplaceholder.typicode.com/nonexistent"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.reason}")
