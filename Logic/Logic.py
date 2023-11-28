# Get user input for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Compare the two integers using if, elif, and else statements
if num1 > num2:
    # If num1 is greater than num2
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    # If num2 is greater than num1
    print(f"{num2} is larger than {num1}")
else:
    # If both numbers are equal
    print("Both numbers are equal")
