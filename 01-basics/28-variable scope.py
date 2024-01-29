# In Python, the scope of a variable refers to the region of the code where the variable is accessible. The scope determines the visibility and lifetime of a variable. Python has three main types of variable scopes: local scope, global scope, and nonlocal scope.

# Local Scope: Variables defined inside a function have a local scope. They are only accessible within that function. Once the function execution is complete, the local variables are destroyed and cannot be accessed from outside the function. Here's an example:
def my_function():
    x = 10  # local variable
    print(x)

my_function()  # Output: 10
print(x)  # Raises NameError: name 'x' is not defined

# In the above example, the variable x is defined inside the my_function() function and can only be accessed within that function.
# Global Scope: Variables defined outside of any function or at the top level of a module have a global scope. They can be accessed from anywhere in the code, including inside functions. Global variables persist throughout the entire program execution. Here's an example:

x = 10  # global variable

def my_function():
    print(x)

my_function()  # Output: 10
print(x)  # Output: 10

# In the above example, the variable x is defined outside the function and can be accessed both inside and outside the function.


# Nonlocal Scope: Nonlocal variables are used in nested functions, where a variable defined in the enclosing function is accessed by the nested function. It allows the nested function to modify the value of the variable in the enclosing function. Here's an example:

def outer_function():
    x = 10  # outer function variable

    def inner_function():
        nonlocal x
        x = 20  # modifies the outer function variable
        print(x)

    inner_function()  # Output: 20
    print(x)  # Output: 20

outer_function()

# In the above example, the nonlocal keyword is used to indicate that the variable x is defined in the outer function and should be modified by the inner function.


# It's important to note that the order of variable resolution in Python follows the LEGB rule: Local, Enclosing (nonlocal), Global, and Built-in scopes. This means that Python first searches for a variable in the local scope, then in the enclosing scope, followed by the global scope, and finally in the built-in scope.
