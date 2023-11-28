# Taking three integers as input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))


# Comparing the integers using 'if', 'elif', and 'else' statements
if (
    num1 != num2 and num1 != num3 and num2 != num3
):  # Checking if all numbers are different
    if num1 > num2 and num1 > num3:  # Checking if num1 is the largest
        print(f"{num1} is the largest number.")
    elif num2 > num1 and num2 > num3:  # Checking if num2 is the largest
        print(f"{num2} is the largest number.")
    else:  # If above conditions are not satisfied, num3 must be the largest
        print(f"{num3} is the largest number.")
else:
    print("Please enter three different numbers.")
