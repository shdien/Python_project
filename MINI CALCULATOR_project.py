#MINI CALCULATOR 

first = input("enter first number:=")
operator = input("enter a operator (+,-,*,/,%,**):=")
seconed = input("enter seconed number:=")

first = float(first)
seconed = float(seconed)

if operator == "+":
    print(first+seconed)
elif operator == "-":
    print(first-seconed)
elif operator == "*":
    print(first*seconed)
elif operator == "/":
    print(first/seconed )
elif operator == "%":
    print(first%seconed)
elif operator == "**":
    print(first**seconed)
else:
    print ("operator invalid")

