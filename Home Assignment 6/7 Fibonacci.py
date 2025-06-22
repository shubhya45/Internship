# 7.	Fibonacci Generator
# Function fibonacci(n) returns a list of first n Fibonacci numbers.

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
print(fibonacci(5))
