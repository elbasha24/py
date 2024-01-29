# Keyword arguments in Python allow you to pass arguments to a function using the key-value syntax. This means that when calling a function, you can specify the argument names along with their corresponding values. The order of the arguments doesn't matter as long as you provide the argument names.
# Here's an example to illustrate the usage of keyword arguments:

def greet(name, age):
    print("Hello", name)
    print("You are", age, "years old")
greet("Omar",13)

# greet(name="Alice", age=25)

# In the example above, the greet function takes two keyword arguments: name and age. When calling the function, we specify the argument names (name= and age=) along with their values ("Alice" and 25). This allows us to pass the arguments in any order we want.

# Using keyword arguments can make your code more readable and self-explanatory, especially when a function has multiple parameters. It also provides flexibility in case you want to specify only some of the arguments and leave others with their default values.
# It's important to note that keyword arguments are not limited to a specific number. You can pass as many keyword arguments as needed when calling a function.


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Alice", age=25, city="New York")

# default positional function arguments.

def greet2(name="Nasr", age=12):
    print("Hello", name)
    print("You are", age, "years old")

greet2()
