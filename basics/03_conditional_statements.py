# Lab Task: Conditional Statements (if-else)

# 1. Simple condition
x = 1
if x > 0:
    print("x is positive")

# 2. Comparing two numbers from user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Checking comparison cases (including equal condition)
if num1 > num2:
    print("First number is greater than second number")
elif num1 < num2:
    print("First number is less than second number")
else:
    print("Both numbers are equal")
