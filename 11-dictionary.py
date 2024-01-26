# definition of dictionary in python
# //dictionary is a collection data type that stores key-value pairs.
# //It is an unordered collection of items. Each item in the dictionary has a unique
# //key and corresponds to a value. The keys are immutable, but the values can be
# //changed. In Python dictionaries are written with curly brackets {}.

names = {1:"Nasr",2:"Mona",3:"Shahd",4:"Malak",5:"Omar"}

for  i in names:
    print(i,"--->",names[i])
    print("----------------------------")

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Loop through keys and values
for key, value in my_dict.items():
    print(key, value)

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Loop through keys only
for key in my_dict:
    print(key)

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Loop through values only
for value in my_dict.values():
    print(value)

namez = {1:"Nasr",2:"Mona",3:"Shahd",4:"Malak",5:"Omar"}
for key,value in namez.items():
    print(key,value)

# add an item to dictionary
namez.update({6:"koko"})

print(namez.keys())
# print keys
print(namez.values())
# print values
print(namez.items())
