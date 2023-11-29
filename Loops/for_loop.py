# Example 1: Iterating through a list
fruits = ["apple", "banana", "cherry"]
print("Example 1: Iterating through a list")
for fruit in fruits:
    print(fruit)
print()

# Example 2: Iterating through a string
message = "Hello, Python!"
print("Example 2: Iterating through a string")
for char in message:
    print(char)
print()

# Example 3: Iterating through a range of numbers
print("Example 3: Iterating through a range of numbers")
for i in range(5):
    print(i)
print()

# Example 4: Using range() to iterate over a specific range of numbers
print("Example 4: Using range() to iterate over a specific range of numbers")
for num in range(2, 10, 2):  # range(start, stop, step)
    print(num)
print()

# Example 5: Iterating through a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "country": "USA"
}
print("Example 5: Iterating through a dictionary")
for key, value in person.items():
    print(f"{key}: {value}")
print()

# Example 6: Nested loops
print("Example 6: Nested loops")
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
print()

# Example 7: Using break statement within a loop
print("Example 7: Using break statement within a loop")
for i in range(5):
    if i == 3:
        break
    print(i)
print()

# Example 8: Using continue statement within a loop
print("Example 8: Using continue statement within a loop")
for i in range(5):
    if i == 2:
        continue
    print(i)
print()

# Example 9: Using else block with for loop
print("Example 9: Using else block with for loop")
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")
