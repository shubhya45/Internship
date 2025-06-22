# Part A: Functional Thinking
# 1.	Greeting Based on Time
# Define a function greet_user(hour) that:
# o	Takes current hour (24-hr format)
# o	Prints:
# 	"Good Morning" if 5–12
# 	"Good Afternoon" if 12–17
# 	"Good Evening" if 17–21
# 	"Good Night" otherwise

def greet_user(hour):
    if 5 <= hour < 12:
        print("Good Morning")
    elif 12 <= hour < 17:
        print("Good Afternoon")
    elif 17 <= hour < 21:
        print("Good Evening")
    else:
        print("Good Night")