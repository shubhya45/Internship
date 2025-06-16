# 7.	Write a small calculator program:
# o	Ask user to enter two numbers and an operator (+, -, *, /)
# o	Based on the operator, perform and display the result
# Enter first number: 10
# Enter second number: 5
# Enter operator: *
# Output: 10 * 5 = 50

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operator = input("Enter operator(+, -, *, /) : ")


if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2 
else:
    result = "Invalid operator"

print(f"{num1} {operator} {num2} = {result}")
