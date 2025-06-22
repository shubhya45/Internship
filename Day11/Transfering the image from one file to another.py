with open(r"C:\Users\Dell\Pictures\Screenshots\Screenshot 2025-06-10 160813.png","rb") as file:
    readD=file.read()

with open("Image.jpg","wb") as file:
    file.write(readD)

