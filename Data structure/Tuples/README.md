
```markdown
# Tuples in Python

Tuples in Python are ordered collections of elements enclosed within parentheses `()`. They are similar to lists but are immutable, meaning their elements cannot be changed after creation.

## Creating a Tuple
To create a tuple, enclose elements within parentheses and separate them with commas.

```python
my_tuple = (1, 2, 3, 'apple', 'banana')
```

## Accessing Elements
Elements within a tuple can be accessed using index values starting from 0.

```python
print(my_tuple)       # Output: (1, 2, 3, 'apple', 'banana')
print(my_tuple[0])    # Output: 1
print(my_tuple[3])    # Output: 'apple'
```

## Key Points about Tuples
- Tuples can contain elements of different data types.
- Elements within a tuple are indexed starting from 0.
- Tuples are immutable; their elements cannot be modified after creation.
- Tuples are useful for storing fixed collections of data.

Tuples are commonly used when you want to store a collection of items that should not be changed, such as coordinates, database records, or any other immutable sequence of values.
```
