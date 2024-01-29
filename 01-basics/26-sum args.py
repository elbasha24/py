# In the function above, *args is used to accept a varying number of positional arguments. The sum() function is then used to calculate the sum of all the arguments passed to the function.

def sum_arguments(*args):
    return sum(args)
print(sum_arguments(12,13,13,15))

