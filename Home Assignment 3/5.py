# 5.	Ask the user to enter a number between 100 and 500:
# 	Use logical operators to validate the input range.

num = int(input(" Enter the number between (100 to 500) : "))

if num > 100 and num < 500:
    print(num)
else:
    print(" Invalid number ..")