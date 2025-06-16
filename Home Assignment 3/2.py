# 🔹 Part B: Comparison Operators
# 2.	Take age as input from the user and check if:
# o	The person is 18 or older
# o	The person is a senior citizen (>= 60)

age = int(input("Enter age  : "))
if age >= 18:
    print("You are 18 or older.")
    if age >= 60:
        print("You are a senior citizen.")
else:
    print("You are not 18 or older.")

