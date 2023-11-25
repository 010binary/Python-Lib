````markdown
# Python Basics README

## File Types in Python

Python files commonly use the extension `.py`.

## String Literals

Strings in Python are denoted by double quotes (`" "`) or single quotes (`' '`). Anything enclosed within these quotes is considered a string, for example: `"Alpha"`, `'22'`, etc.

## Operators

Python operators include: `+, -, *, **, /, //, %, ** ½`. These operators are similar to those used in mathematics.

## Output

To display output in Python, the `print()` function is used.

## Variables and Values

Variables in Python store values or references. Variables are assigned using the format: `variable = value`, for example: `name = "John"`, `age = 25`, etc.

### Rules for Naming Variables

- Variable names can contain letters, numbers, or underscores (`_`).
- Variable names cannot start with a number.
- Spaces are not allowed; snake_case is preferred.
- Variable names cannot be a Python keyword (`def`, `break`, `try`, `finally`, etc.).
- Ideally, variable names should be short and descriptive.
- Python is case-sensitive.

## Comments

Comments in Python are created using the pound symbol (`#`) followed by the comment text. For example: `# This is a comment`.

## Writing Your First Python Code

```python
greeting = "hello world"
print(greeting)  # Output: hello world
```
````

Python code is executed sequentially from top to bottom.

## Data Types in Python

1. **String**: Used for storing text data.
2. **Integer**: Used for whole numbers.
3. **Float**: Used for decimal numbers.
4. **Boolean**: Represents logic (`True` or `False`).

## Reassignment of Variables

Variables can be reassigned new values after their initial assignment, for example:

```python
greeting = "good morning"
greeting = "hello world"
print(greeting)  # Output: hello world
```

## Variable Naming Conventions

- Must start with a letter.
- Can contain letters, numbers, or underscores.
- Shouldn't use Python keywords or syntax.
- Use snake_case for readability.
- Should be short and descriptive.
- Python is case-sensitive.

## Printing to the Console

The `print()` function is used to display output in the console.

## Concatenation

Strings and other data types can be concatenated using the `+` operator. For example:

```python
example_string = "you are "
example_int = 12
example_string2 = " years old."
print(example_string + str(example_int) + example_string2)  # Output: you are 12 years old
```

Multiplying a string with an integer replicates the string that many times.

### Supported Concatenation/Operations

- String + String: Concatenation
- String + Integer: Concatenation
- String + Float: Concatenation
- String \* Integer: Replication

Note: A string can only be multiplied by an integer; any other operation will result in an error.

```

```
