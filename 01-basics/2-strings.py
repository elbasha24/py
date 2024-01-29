# strings in python
# //https://www.w3schools.com/python/gloss_py_string
# string methods:
#   capitalize() - Converts the first character of a string to uppercase (cap
#   lower()     - Returns a copy of the string, converting all characters to lowercase
#   upper()     - Returns a copy of the string, converting all characters to uppercase
#   split(sep)   - Splits a string into a list where each word is
#                  a list item. separator sep is optional. Default separator is a white space.
#   join(sep)    - Joins a sequence of strings using the specified separator.
#   find(sub,start=0,end=None) - Finds the position of
#                                substring sub in the given string. It returns
#                                -1 if substring is not found.
#                                start and end are optional. They define the range in which to search for the substring
#                                start and end are optional positions.
#   index(sub [,start [,end]]) - Like find(), but raises an
#                                 exception if substring is not found.
#   count(sub [,start [,end]] ) - Return the number of non-
#                                 overlapping occurrences of substring sub in
#                                 string, between optional start and end.
#                                 If start or end is not provided it defaults to beginning or end of the string.
#                                 If not found, return 0.
#   replace(old, new[,count]) - Replace occurrences of substring old with
#                               new. If count is given, replace at most this many
#                               occurrences.
#   strip([chars])             - Remove leading and trailing whitespaces
#                                from a string. If chars is provided, it will remove these
#                                characters instead of spaces.
#   lstrip([chars])            - Remove leading whitespaces from a string.
#                                If chars is provided, it will remove these characters
#                                instead of spaces.
#   rstrip([chars])           - Remove trailing whitespaces from a string.
#                                If chars is provided, it will remove these characters
#                                instead of spaces.
#   startswith(prefix[,start[,end]]) - Check if a string starts with prefix.
#                                       It returns True or False.
#   endswith(suffix[,start[,end]]) - Check if a string ends with
#                                 suffix. It returns True or False.
#   isalpha()      - Returns True if all characters in the string are alphabets
#   isdigit()      - Returns True if all characters in the string are digits
#   islower()      - Returns True if all characters in the string are lower case letters
#   isupper()      - Returns True if all characters in the string are upper case letters
#   istitle()      - Returns True if the string consists of words separated by
#                   title underlines.
#   expandtabs(tabsize = 8) - Replace tabs in the string with tab size
#                              spaces. The default tab size is 8.
#   swapcase()     - Swap case of all characters in the string i.e.,
#                   convert all uppercase characters to lowercase and vice versa.
#   capitalize()   - Make the first character of the string to be capitalized.
#   maketrans(x, y [, z]) - Returns a translation table that can
#                            be used with the translate method.
#                            If only one argument is supplied,
#                            it must be a dictionary returned by
#                            maketrans().
#   translate(table)        - Translate characters using the given mapping
#                             table which should have been created by the
#                             maketrans() function. Undefined characters
#                             are left unchanged. The table may specify
#                             None for any character that needs no
#                             translation or defines a specific translation.
#   encode(encoding="utf-8", errors=None) - Encode the string using
#                                          the specified encoding. Defaults
#                                          to UTF-8. May raise UnicodeError
#                                          if the input contains non-UTF
#                                          data.
#   decode(encoding="utf-8", errors=None) - Decode the string using
#                                          the specified encoding. Defaults
#                                          to UTF-8. May raise UnicodeError
#                                          if the input contains invalid
#                                          encoded data.
#   format_map(mapping)    - Format the string using substitutions from the
#                            mapping. The substitutions are identified by {key}
#                            where key is a specification like {name}, or
#                            {name:format}. In the latter case, format is
#                            strftime-style formatting.
#   count(sub, start=0, end=sys.maxsize) - Return the
#                                         number of non-overlapping occurrences
#                                         of substring sub in range [start,end).
#                                         If not found, return 0.
#   find(sub, start=0, end=sys.maxsize) - Find the
#                                           lowest index in the string where substring sub is found;
#                                           otherwise the lowest index where the
#                                           corresponding suffix of sub is found.
#                                           It returns -1 on a mismatch.
#   rfind(sub, start=0, end=sys.maxsize) – Same
#                                            as find() but search backwards.
#                                            Returns -1 on a mismatch.
#   index(sub, start=0, end=sys.maxsize) – Like
#                                              find() but raises an IndexError when the substring is not found.
# Creating a string
my_string = "Hello, World!"

# Displaying the string
print(my_string)

# Accessing individual characters
print(my_string[0])  # Output: H
print(my_string[-1])  # Output: !

# Concatenating strings
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, Alice!

# Getting the length of a string
length = len(my_string)
print(length)  # Output: 13

print(my_string.format())
print(my_string.count('l'))
print(my_string.index('l'))
# return the index of letter L
# print(my_string.rindex('o'))
# Slicing a string
print(my_string[6:9])  # Output: Wor
print(my_string[:9])  # Output: Hello, W
print(my_string[9:])  # Output: rld!
print("".join(["H", "e", "l", "l", "o"]
              ))  # Output: Hello
# Checking if a substring exists within a string
print("lo" in my_string)  # Output: True
print("Hi" not in my_string)  # Output: True
# String methods that don’t change the original string can be called with or without parentheses.
# Methods that do modify the string must always be called with parentheses.
print(my_string.lower())  # Output: hello, world!
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.title())  # Output: Hello, World!</s>
print(my_string.isalnum())
# is alpha numeric
print(my_string.expandtabs(),"129")
