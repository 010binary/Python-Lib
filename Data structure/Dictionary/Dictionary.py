# !/usr/bin/env python

# Creating a basic dictionary
basic_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "email": "alice@example.com"
}

print(type(basic_dict))

# Accessing values in the dictionary
print("Name:", basic_dict["name"])
print("Age:", basic_dict["age"])
print("City:", basic_dict["city"])
print("Email:", basic_dict["email"])

# Modifying a value in the dictionary
basic_dict["age"] = 32
print("Updated Age:", basic_dict["age"])

# Adding a new key-value pair
basic_dict["occupation"] = "Engineer"
print("Occupation:", basic_dict["occupation"])


# Deleting a key-value pair
del basic_dict["email"]
# Or using pop() method to remove and return the value
# removed_email = basic_dict.pop("email")

# Displaying the updated dictionary
print("Updated Dictionary:", basic_dict)


