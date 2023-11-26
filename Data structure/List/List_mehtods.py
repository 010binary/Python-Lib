# Creating a basic list in Python
my_list = [1, 2, 3, 4, 5]

# 20 most commonly used list methods

# 1. append(): Add an element to the end of the list
my_list.append(6)

# 2. extend(): Extend the list by appending elements from an iterable
my_list.extend([7, 8, 9])

# 3. insert(): Insert an element at a specific index
my_list.insert(0, 0)

# 4. remove(): Remove the first occurrence of a value from the list
my_list.remove(3)

# 5. pop(): Remove and return an element at a given index (by default, the last element)
popped_element = my_list.pop(2)

# 6. index(): Return the index of the first occurrence of a value
index_of_5 = my_list.index(5)

# 7. count(): Return the number of occurrences of a value
count_4 = my_list.count(4)

# 8. sort(): Sort the list in ascending order
my_list.sort()

# 9. reverse(): Reverse the elements of the list
my_list.reverse()

# 10. copy(): Return a shallow copy of the list
copied_list = my_list.copy()

# 11. clear(): Remove all elements from the list
my_list.clear()

# 12. len(): Return the number of elements in the list
length_of_list = len(my_list)

# 13. max(): Return the maximum value in the list
maximum_value = max(copied_list)

# 14. min(): Return the minimum value in the list
minimum_value = min(copied_list)

# 15. sum(): Return the sum of all elements in the list
sum_of_elements = sum(copied_list)

# 16. any(): Return True if any element in the list is True
any_true = any([False, True, False])

# 17. all(): Return True if all elements in the list are True
all_true = all([True, True, True])

# 18. join(): Join elements of a list into a string
list_of_strings = ["Hello", "world"]
joined_string = " ".join(list_of_strings)

# 19. index(): Return the index of the first occurrence of a value
index_of_1 = copied_list.index(1)

# 20. clear(): Remove all elements from the list
copied_list.clear()

# Displaying final list or results
print("Updated list after operations:", copied_list)
print("Popped element:", popped_element)
print("Index of 5:", index_of_5)
print("Count of 4:", count_4)
print("Length of list:", length_of_list)
print("Maximum value:", maximum_value)
print("Minimum value:", minimum_value)
print("Sum of elements:", sum_of_elements)
print("Any True:", any_true)
print("All True:", all_true)
print("Joined string:", joined_string)
print("Index of 1:", index_of_1)
