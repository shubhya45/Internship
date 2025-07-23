# Get a Random Dog Image
# API: https://dog.ceo/api/breeds/image/random
# Goal: Fetch and print the image URL (bonus: open it in the browser with webbrowser.open())
import requests
import webbrowser

# Fetch random dog image
dog = requests.get("https://dog.ceo/api/breeds/image/random").json()

# Print image URL
print("Here's a random dog image:")
print(dog["message"])

# Bonus: Open image in web browser
webbrowser.open(dog["message"])
