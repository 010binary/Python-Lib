# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "email": "alice@example.com",
    "buddy" : True
}

# 1. copy(): Create a shallow copy of the dictionary
copied_dict = my_dict.copy()

# 2. clear(): Remove all key-value pairs from the dictionary
my_dict.clear()

# 3. popitem(): Remove and return an arbitrary key-value pair as a tuple
removed_item = copied_dict.popitem()

# 4. pop(key): Remove the key-value pair with the specified key and return the value
removed_email = copied_dict.pop("email")

# 5. update(): Update the dictionary with key-value pairs from another dictionary or iterable
copied_dict.update({"occupation": "Engineer", "age": 32})

# 6. get(): Retrieve the value for a given key, returns None if the key is not found
retrieved_age = copied_dict.get("age")

# 7. items(): Return a view object that displays a list of tuple pairs (key, value)
items_view = copied_dict.items()

# 8. values(): Return a view object that displays a list of all the values in the dictionary
values_view = copied_dict.values()

# 9. keys(): Return a view object that displays a list of all the keys in the dictionary
keys_view = copied_dict.keys()

# Displaying the updated dictionary and other results
print("Copied Dictionary:", copied_dict)
print("Removed Item:", removed_item)
print("Removed Email:", removed_email)
print("Retrieved Age:", retrieved_age)
print("Items View:", items_view)
print("Values View:", values_view)
print("Keys View:", keys_view)


# Any other major one you need please google it 😂😂Dumbass