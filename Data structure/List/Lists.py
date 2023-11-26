# Creating a basic list in Python
list_type = [1, 2, 3, 4, 5]
print(type(list_type))

# Displaying the list elements
print("Elements of the list:")
print(list_type)

# Adding elements to the list
list_type.append(6)
list_type.append(7)

# Displaying the updated list
print("\nUpdated list after adding elements:")
print(list_type)

# Removing elements from the list
list_type.remove(3)  # Remove the element 3
element_removed = list_type.pop()  # Remove the last element and store it in a variable

# Displaying the list after removal
print("\nList after removing elements:")
print(list_type)
print("Element removed:", element_removed)

# Accessing specific elements by index
print("\nAccessing elements by index:")
print("Element at index 0:", list_type[0])
print("Element at index 2:", list_type[2])
