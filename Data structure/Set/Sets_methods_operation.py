# Set Operations and Methods

# Create sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (|)
union_set = set1 | set2
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection (&)
intersection_set = set1 & set2
print("Intersection:", intersection_set)  # Output: {3}

# Difference (-)
difference_set = set1 - set2
print("Difference:", difference_set)  # Output: {1, 2}

# Symmetric Difference (^)
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Add elements (add())
set1.add(4)
print("Add Element:", set1)  # Output: {1, 2, 3, 4}

# Remove an element (remove())
set1.remove(2)
print("Remove Element:", set1)  # Output: {1, 3, 4}

# Discard an element (discard())
set1.discard(5)  # No error if element doesn't exist
print("Discard Element:", set1)  # Output: {1, 3, 4}

# Clear a set (clear())
set2.clear()
print("Cleared Set:", set2)  # Output: set()

# Check if subset (<=)
subset_check = set1 <= {1, 3, 4, 5}
print("Subset Check:", subset_check)  # Output: True

# Check if superset (>=)
superset_check = set1 >= {1, 3}
print("Superset Check:", superset_check)  # Output: True

# Check if disjoint (isdisjoint())
disjoint_check = set1.isdisjoint({2, 5})
print("Disjoint Check:", disjoint_check)  # Output: True

# Copy a set (copy())
copied_set = set1.copy()
print("Copied Set:", copied_set)  # Output: {1, 3, 4}

# Length of a set (len())
length_set1 = len(set1)
print("Length of set1:", length_set1)  # Output: 3


