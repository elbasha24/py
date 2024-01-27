# Reading from a File: Once a file is opened, you can read its contents using various methods. The most common method is read(), which reads the entire content of the file as a string. Alternatively, you can use readline() to read a single line or readlines() to read all lines into a list. Here's an example of reading the contents of a file:

# file = open("/home/nk/Documents/test.txt", "r")
# content = file.read()
# print(content)
# file.close()

file = open("/home/nk/Documents/test.txt", "w")
file.write("Hello, Nasr!")
file.close()

file = open("/home/nk/Documents/test.txt", "a")
file.write("Appending new content!")
file.close()


with open("/home/nk/Documents/test.txt", "r") as file:
    content = file.read()
    print(content)




# Working with Files in Python

# Working with files is an essential part of programming in Python. Python provides built-in functions and modules to handle file input and output operations. Here are the basic steps to work with files in Python:


# Opening a File: To open a file, you can use the open() function, which takes two parameters: the file path and the mode in which you want to open the file. The mode can be "r" for reading, "w" for writing, "a" for appending, or "x" for creating a new file. For example, to open a file named "example.txt" in read mode, you can use the following code:

# file = open("example.txt", "r")
# Reading from a File: Once a file is opened, you can read its contents using various methods. The most common method is read(), which reads the entire content of the file as a string. Alternatively, you can use readline() to read a single line or readlines() to read all lines into a list. Here's an example of reading the contents of a file:

# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()
# Writing to a File: To write to a file, you need to open it in write mode ("w"). This mode will create a new file if it doesn't exist or overwrite the existing file. You can use the write() method to write content to the file. Here's an example:

# file = open("example.txt", "w")
# file.write("Hello, World!")
# file.close()
# Appending to a File: If you want to add content to an existing file without overwriting it, you can open the file in append mode ("a"). This mode will position the file pointer at the end of the file. Here's an example:

# file = open("example.txt", "a")
# file.write("Appending new content!")
# file.close()
# Closing a File: It's important to close a file after you're done working with it to free up system resources. You can use the close() method to close the file. Alternatively, you can use the with statement, which automatically closes the file for you. Here's an example using the with statement:

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)










