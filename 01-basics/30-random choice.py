

import random
names=["omar","Malak","Shahd","Mona","Nasr"]
selectname=random.choice(names)
print(selectname)

Cities=["Cairo","Doha","Bahrain"]
SelectCity=random.choice(Cities)
print(SelectCity)
# print(random.shuffle(Cities))


# Set the random seed
random.seed(42)

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)

# Generate a random integer within a range
random_number = random.randrange(1, 10)
print("Random number:", random_number)

# Generate a random float from a normal distribution
random_float = random.normalvariate(0, 1)
print("Random float from a normal distribution:", random_float)

# Generate a random byte string
random_bytes = random.randbytes(4)
print("Random bytes:", random_bytes)

# Get the current state of the random generator
state = random.getstate()
print("Current state:", state)

# Set the state of the random generator to a previous state
random.setstate(state)

# Generate a random number using the restored state
restored_random_number = random.randrange(1, 10)
print("Restored random number:", restored_random_number)

