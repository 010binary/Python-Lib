# Example 1: Simple while loop
print("Example 1: Simple while loop")
num = 1
while num <= 5:
    print(num)
    num += 1
print()

# Example 2: Using while loop with user input
print("Example 2: Using while loop with user input")
user_input = input("Enter 'exit' to stop: ")
while user_input.lower() != "exit":
    print(f"Entered: {user_input}")
    user_input = input("Enter 'exit' to stop: ")
print()

# Example 3: Using while loop for a specific condition
print("Example 3: Using while loop for a specific condition")
num = 10
while num > 0:
    print(num)
    num -= 2
print()

# Example 4: Using while loop with break statement
print("Example 4: Using while loop with break statement")
num = 1
while True:
    print(num)
    num += 1
    if num > 5:
        break
print()

# Example 5: Using while loop with continue statement
print("Example 5: Using while loop with continue statement")
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
print()

# Example 6: Using else block with while loop
print("Example 6: Using else block with while loop")
num = 1
while num <= 5:
    print(num)
    num += 1
else:
    print("Loop completed successfully")
