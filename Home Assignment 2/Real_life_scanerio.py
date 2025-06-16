# Part D: Real-Life Scenario
# 6.	Create a small bill calculator:
# o	Input: item name, quantity, price per item
# o	Output: total cost = quantity × price
# Example:
# Enter item: Pen
# Enter quantity: 3
# Enter price per item: 15
# Output: Total cost for 3 Pens is ₹45
# ________________________________________

item_name = input(" Enter item name : ")
quantity = int(input(" Enter quantity of item : "))
price= int(input(" Enter price( per item ): "))

Total_cost = quantity * price

print(f" Total cost for {quantity} {item_name} is : {Total_cost}")