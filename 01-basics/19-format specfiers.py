# In Python, format specifiers are used to control the formatting of values when they are inserted into a string. They follow the field name and are separated by a colon (:) character. Here are some commonly used format specifiers:
# %d: Used to format integers as strings within the context of the old-style string formatting method .
# %s: Used to format strings within the context of the old-style string formatting method.
# %f: Used to format floating-point values within the context of the old-style string formatting method.
# %x: Used to format integers as hexadecimal strings within the context of the old-style string formatting method.
# %o: Used to format integers as octal strings within the context of the old-style string formatting method.
# In addition to the old-style string formatting, Python also provides newer string formatting techniques using the .format() method and f-strings. Here are some examples:
# .format() method: With the .format() method, you can use curly braces {} as placeholders for values that will be inserted into the string. Format specifiers can be added after the colon (:) inside the curly braces to control the formatting. For example:

name = "John"
age = 23
print("Hello, {}!".format(name))  # Output: Hello, John!
print("{} is {} years old.".format(name, age))  # Output: John is 23 years old.

# f-strings: F-strings provide a concise and convenient way to embed Python expressions inside string literals for formatting. They are prefixed with the letter 'f' and allow you to directly include variables and expressions inside curly braces {}. For example:
name = "John"
age = 23
print(f"Hello, {name}!")  # Output: Hello, John!
print(f"{name} is {age} years old.")  # Output: John is 23 years old.


