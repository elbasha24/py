import os

# Check if a file exists
if os.path.exists("file.txt"):
    print("The file exists")
else:
    print("The file does not exist")

# Create a directory
os.mkdir("my_directory")

# List all files and directories in a directory
print(os.listdir())

# Rename a file
os.rename("old_file.txt", "new_file.txt")

# Delete a file
os.remove("file.txt")

# Change the current working directory
os.chdir("new_directory")

# Get the current working directory
print(os.getcwd())


# To move, copy, and delete files in Python, you can use the shutil module, which provides convenient methods for file operations. Here's how you can perform these operations:


# Moving a File:

# To move a file from one location to another, you can use the shutil.move() function. This function takes two parameters: the source file path and the destination file path. Here's an example:


# import shutil

# source = '/path/to/source/file.txt'
# destination = '/path/to/destination/file.txt'

# shutil.move(source, destination)

# In this example, the file located at source will be moved to the destination path.


# Copying a File:

# To copy a file, you can use the shutil.copy() function. This function also takes two parameters: the source file path and the destination file path. Here's an example:


# import shutil

# source = '/path/to/source/file.txt'
# destination = '/path/to/destination/file.txt'

# shutil.copy(source, destination)

# In this example, the file located at source will be copied to the destination path.


# Deleting a File:

# To delete a file, you can use the os.remove() function from the built-in os module. This function takes the file path as a parameter. Here's an example:


# import os

# file_path = '/path/to/file.txt'

# os.remove(file_path)

# In this example, the file located at file_path will be deleted.


# Remember to handle exceptions and ensure that the file paths are correct before performing these operations.


# Please note that the shutil module also provides additional functions for more advanced file operations, such as copying entire directories (shutil.copytree()) and deleting directories (shutil.rmtree()).
