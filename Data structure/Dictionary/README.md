
```markdown
# Python Dictionary Basics

## Introduction to Dictionaries
A dictionary in Python is a collection of key-value pairs enclosed in curly braces `{}`. Each key is associated with a value, allowing easy retrieval of values using their corresponding keys.

### Creating a Basic Dictionary
```python
basic_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "email": "alice@example.com"
}
```

### Accessing Values in the Dictionary
Values within a dictionary are accessed using square brackets with the associated key (`basic_dict["key"]`).

### Modifying Values in the Dictionary
```python
basic_dict["age"] = 32
```

### Adding a New Key-Value Pair
```python
basic_dict["occupation"] = "Engineer"
```

### Deleting a Key-Value Pair
```python
del basic_dict["email"]
# Or using pop() method
# removed_email = basic_dict.pop("email")
```

### Displaying the Updated Dictionary
```python
print("Updated Dictionary:", basic_dict)
```

## Ten Most Used Methods on Dictionaries

### 1. `keys()`
Returns a view of all the keys in the dictionary.

### 2. `values()`
Returns a view of all the values in the dictionary.

### 3. `items()`
Returns a view of all the key-value pairs in the dictionary.

### 4. `get(key)`
Returns the value associated with the given key. Returns `None` if the key is not found (or specified default).

### 5. `update(dictionary)`
Merges the elements of another dictionary into the current dictionary.

### 6. `pop(key)`
Removes the specified key and returns its corresponding value.

### 7. `popitem()`
Removes and returns the last key-value pair as a tuple.

### 8. `clear()`
Removes all elements from the dictionary.

### 9. `copy()`
Returns a shallow copy of the dictionary.

### 10. `fromkeys(iterable, value)`
Creates a new dictionary with keys from the iterable and values set to the specified value.

For more details and examples on these methods, refer to the Python documentation or online resources.

Use these methods to manipulate and extract information from dictionaries effectively in Python.
```
