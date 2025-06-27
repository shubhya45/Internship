# 🔹 Part E: Explore and Practice
# 10.	Import the os module:
# o	List all files in the current directory.
# o	Get the current working directory.

import os

print("Files in the current directory ")
for file in os.listdir('.'):
    print(file)

print("Current working directory: ", os.getcwd())