# list in python
#//https://www.geeksforgeeks.org/list-in-python/
# List is a collection of items that can be of different data types, and they are ordered.
# Creating an empty list:
my_list = []                    # Empty list
print("Empty List : ", my_list)
# Adding elements to the list using append() method:
my_list.append(10)              # Adds 10 at the end of the list
my_list.append('Hello')         # Adds 'Hello' at the end of the list
my_list.append([1,2,3])        # Adds [1,2,3] at the end of the list
# print statement will show all the elements in the list
print("After appending : ", my_list)
# Accessing Elements from the list:
# We use indexing for accessing element by its index position. Indexing starts with 0 for the first
# element and goes till (n-1) where n is the number of elements present in the list
print("Accessing Elements : ")
print("Element at index 0 :", my_list[0])   # Output: 10
print("Element at index 1 :", my_list[1])   # Output: Hello
print("Element at index 2 :", my_list[2])   # Output: [1,2,3]
print("\n")
# Slicing in Python lists:
# Syntax : list[start:stop:step]
# Here start is inclusive and stop is exclusive. If we don’t provide any value
# then it considers them as None i.e., it means take everything from beginning to
# the end. Step is optional and if not provided then it takes step=1 which means
# take every element.
print("Slice the list : \n")
print("Entire List : ", my_list)
print("List from 1st to last : ", my_list[1:])
print("List from 2nd to last : ", my_list[1:-1])
print("Elements from 1st to 5th : ", my_list[:5])
print("Elements from 6th to last : ", my_list[6:])
print("Elements from 1st to last with step 2 : ", my_list[::2], "\n\n")
# Updating or modifying elements in the list:
# To update or modify an element in the list, we need to access it through its index
# and assign a new value to it.
my_list[0] = "Geek"       # Changing the value of the first element
print("Updated List : ", my_list)
# Checking whether an item exists in the list or not using the in keyword:
print("Checking membership : ")
print(7 in my_list)      # False
print("Hello" in my_list) # True
# Removing/deleting an element from a list using the remove() method:
my_list.remove(10)        # Remove the first occurrence of 10
print("Removed 10 : ", my_list)
# Using pop() method to remove an element by reference:
# It removes the element by reference so that next time when you try to access
# this element it will give an error because the element has been removed.
val = my_list.pop(1)     # Pop the element at index 1
print("Popped Value : ", val)
print("After Popping : ", my_list)
# Using append() method to add an element at the end of the list:
my_list.append(10)         # Adding 10 at the end of the list
print("Appended List : ", my_list)
# Using insert() method to add an element at a specific position:
my_list.insert(3, "World")  # Inserting World at index 3
                            # So now the list becomes ['Geek', 'Hello', '[', 'World']
print("Inserted List : ", my_list)
# Sorting the list:
# The sort() function sorts the list in ascending order.
my_list.sort()             # ['Geek', 'Hello', 'Python', 'Programming', 'is', 'fun!', 'World']
print("Sorted List : ", my_list)
# Reversing the list:
# The reverse() function reverses the list.
my_list.reverse()          # ['World', 'fun!', 'is', 'Programming', 'Python', 'Hello', '[', 'Geek']
print("Reversed List : ", my_list)
