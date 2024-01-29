squares = [x**2 for x in range(1, 11)]
print(squares)
# Create a list of even numbers from 1 to 20:
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)
# Create a list of uppercase letters from a string:
string = "Hello, World!"
uppercase_letters = [char for char in string if char.isupper()]
print(uppercase_letters)
# Create a list of tuples containing the index and value of each element in a list:
my_list = ['apple', 'banana', 'cherry']
indexed_list = [(index, value) for index, value in enumerate(my_list)]
print(indexed_list)
# Create a list of squared numbers from another list, but only if the number is greater than 5:
numbers = [1, 3, 5, 7, 9, 11]
squared_numbers = [x**2 for x in numbers if x > 5]
print(squared_numbers)
# Create a list of the lengths of words in a sentence, excluding punctuation:
sentence = "Hello, how are you today?"
word_lengths = [len(word) for word in sentence.split() if word.isalpha()]
print(word_lengths)

