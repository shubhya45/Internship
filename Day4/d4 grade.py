m1=int(input("Enter the first number"))
m2=int(input("Enter the second number"))
m3=int(input("Enter the third number"))

total_marks = m1+m2+m3
per =total_marks/3

print("total marks",total_marks )
print("per",per)

if per>90 and per<100:
    print(f"A grade")
elif per>80 and per<90:
    print(f"B grade")
elif per>70 and per<80:
    print("C grade")
elif per>60 and per<70:    
    print(f"First class with distiction")
elif per>50 and per<60:
    print("First class")
elif per>40 and per<50:
    print("Pass")
else:
    print("Fail")