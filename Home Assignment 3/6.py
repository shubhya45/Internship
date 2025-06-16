#  Part D: Expression Evaluation
# 6.	Evaluate the following expressions:
# print(5 + 3 * 2)
# print((5 + 3) * 2)
# print(10 - 3 ** 2 + 4)
# print(100 // 3 % 2)
# o	Write comments explaining why each output is as it is based on operator precedence.

print(5 + 3 * 2)    # 3 * 2 = 6, then 5 + 6 = 11  because * has more pprecidency than + operator

print((5 + 3) * 2)  # (5 + 3) = 8, then 8 * 2 = 16  because () has more pprecidency than * operator

print(10 - 3 ** 2 + 4)  # 3 ** 2 = 9, then 10 - 9 = 1, then 1 + 4 = 5  because ** has more pprecidency than + and -   operator

print(100 // 3 % 2)  # 100 // 3 = 33, then 33 % 2 = 1   because // has more pprecidency than %operator
