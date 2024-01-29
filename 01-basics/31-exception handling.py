import random

try:
    # Generate a random number
    random_number = random.randint(1, 10)

    # Divide a number by zero to raise an exception
    result = 10 / 0

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid value encountered.")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    print("This block always executes, regardless of whether an exception occurred or not.")


# In the above example:


# The try block contains the code that may raise an exception.
# If an exception occurs, it is caught by the corresponding except block based on the type of the exception.
# If the exception does not match any specific except block, it is caught by the generic Exception block.
# The finally block is optional and always executes, regardless of whether an exception occurred or not.

# By using exception handling, you can gracefully handle errors, prevent program crashes, and perform necessary cleanup operations.
