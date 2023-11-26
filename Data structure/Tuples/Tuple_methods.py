my_tuple = ("Hello", 42, 3.14, True, "World", 7.8, False, 50, "people", "break")
int_tuple = (42, 3.14, 7.8, 80, 1, 7)


# 1. len(): Returns the length of the tuple.
len_of_tuple = len(my_tuple)
print("Length of the tuple:", len_of_tuple)

# 2. index(): Returns the index of the first occurrence of a specified value.
index_of_value = my_tuple.index('World')
print("Index of 'World' in the tuple:", index_of_value)

# 3. count(): Counts the number of occurrences of a specified value.
count_of_value = my_tuple.count(True)
print("Count of 'True' in the tuple:", count_of_value)

# 4. Concatenation: Combining two tuples using the '+' operator.
combined_tuple = my_tuple + ('New', 'Tuple')
print("Combined tuple:", combined_tuple)

# 5. Slicing: Extracting a portion of the tuple using slicing operations.
sliced_tuple = my_tuple[2:5]
print("Sliced tuple:", sliced_tuple)

# 6. Membership: Checking if an element exists in the tuple using 'in'.
check_membership = 'people' in my_tuple
print("Check membership of in the tuple:", check_membership)

# 7. Min and Max: Finding the minimum and maximum elements in a tuple.
min_value = min(int_tuple)
max_value = max(int_tuple)
print("Minimum value in the tuple:", min_value)
print("Maximum value in the tuple:", max_value)

# 8. Converting to List: Converting a tuple to a list using the list() function.
tuple_to_list = list(my_tuple)
print("Tuple converted to a list:", tuple_to_list)

# 9. Unpacking: Unpacking tuple elements into separate variables.
var1, var2, var3 = my_tuple[:3]  # Unpacking the first three elements
print("Unpacked variables:", var1, var2, var3)

# 10. Repeating: Repeating the tuple elements using the '*' operator.
repeated_tuple = my_tuple * 2  # Repeats the tuple twice
print("Repeated tuple:", repeated_tuple)

