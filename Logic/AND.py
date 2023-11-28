# Define the three integers
num1 = 10
num2 = 20
num3 = 15

# Compare num1, num2, and num3 to find the largest number
if num1 >= num2 and num1 >= num3:  # Check if num1 is greater than or equal to num2 and num3
    print(f"{num1} is the largest number.")
elif num2 >= num1 and num2 >= num3:  # Check if num2 is greater than or equal to num1 and num3
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")
