# 3	Print the multiplication table of a number (user input).

num = int(input("Enter the number for multiplication table : "))

for i in range(1,11):
    j = num*i
    print(f"{num} * {i} = {j}")