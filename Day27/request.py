# Task:
# Get a Random Joke
# API: https://official-joke-api.appspot.com/random_joke
# Goal: Fetch and display the joke setup and punchline.
import requests

goal = requests.get("https://official-joke-api.appspot.com/random_joke").json()
print("Here's a random joke:")
print(goal["setup"])
print(goal["punchline"])