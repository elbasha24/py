# type casting in python
# Implicit Type Casting:

    # In implicit type casting, Python automatically converts one data type to another without user involvemen

a = 7
print(type(a))  # Output: <class 'int'>

b = 3.0
print(type(b))  # Output: <class 'float'>

c = a + b
print(c)  # Output: 10.0
print(type(c))  # Output: <class 'float'>

d = a * b
print(d)  # Output: 21.0
print(type(d))  # Output: <class 'float'>


# Explicit Type Casting:

    # In explicit type casting, the user needs to manually convert the variable's data type into the required data type.
my_string = "10"
my_integer = int(my_string)  # Explicitly converting string to integer
print(my_integer)  # Output: 10
print(type(my_integer))  # Output: <class 'int'>

my_float = float(my_integer)  # Explicitly converting integer to float
print(my_float)  # Output: 10.0
print(type(my_float))  # Output: <class 'float'>

my_string = str(my_float)  # Explicitly converting float to string
print(my_string)  # Output: "10.0"
print(type(my_string))  # Output: <class 'str'>
