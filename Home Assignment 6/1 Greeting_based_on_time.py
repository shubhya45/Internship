def greet_user(hour):
    if 5 <= hour < 12:
        print("Good Morning")
    elif 12 <= hour < 17:
        print("Good Afternoon")
    elif 17 <= hour < 21:
        print("Good Evening")
    else:
        print("Good Night")


greet_user(9)   
greet_user(13)  
greet_user(18)  
greet_user(23)  