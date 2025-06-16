# 🔹 Part C: Logical Operators
# 4.	Create a login check:
# o	Ask for username and password
# o	If both match predefined values (e.g., "admin" and "1234"), print "Login successful"
# o	Else, print "Invalid credentials"

username = input(" Enter username : ")
passw = input(" Enter password : ")

if username == "admin" and passw == "200":
    print(" Login successful ... ")
else:
    print(" Invalid credentials ")
