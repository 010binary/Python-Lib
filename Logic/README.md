# Logic Statements in Python

## Introduction
Logic statements in Python, specifically `if`, `else if` (or `elif`), and `else` statements, are fundamental for controlling program flow based on conditions. These statements allow the execution of different code blocks depending on whether certain conditions are true or false.

## `if`, `elif`, and `else` Statements
### `if` Statement
The `if` statement is used to execute a block of code only if a specified condition is true.

```python
if condition:
    # code to execute if condition is True
```

### `elif` Statement
The `elif` statement allows checking for additional conditions after the initial `if` statement. It comes after an `if` statement and before an optional `else` statement.

```python
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition1 is False and condition2 is True
```

### `else` Statement
The `else` statement is used to execute a block of code when the preceding conditions in the `if` and `elif` statements are False.

```python
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition1 is False and condition2 is True
else:
    # code to execute if both condition1 and condition2 are False
```

## Logical Operators (`and`, `or`, `not`)
Logical operators (`and`, `or`, `not`) are used to combine conditional statements.

### `and` Operator
The `and` operator returns `True` if both conditions on either side of the operator are true.

```python
if condition1 and condition2:
    # code to execute if both condition1 and condition2 are True
```

### `or` Operator
The `or` operator returns `True` if at least one of the conditions on either side of the operator is true.

```python
if condition1 or condition2:
    # code to execute if either condition1 or condition2 is True
```

### `not` Operator
The `not` operator is used to negate the condition.

```python
if not condition:
    # code to execute if condition is False
```

## Conclusion
Logic statements (`if`, `elif`, `else`) along with logical operators (`and`, `or`, `not`) are powerful tools in Python for controlling program flow based on various conditions, allowing for more dynamic and versatile code execution.