# Creating a set
my_set = {1, 2, 3, 4, 5}  # Using curly braces to define a set
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Trying to add a duplicate element (no change in set)
my_set.add(3)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Creating a set from a list (removes duplicates)
my_list = [2, 2, 4, 4, 6, 6]
set_from_list = set(my_list)
print(set_from_list)  # Output: {2, 4, 6}


print(type(my_set))