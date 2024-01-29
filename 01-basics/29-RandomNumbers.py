import random

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)
print(random_number)

rn=random.randrange(1,12,1)
print(rn)
# random float
rn2=random.betavariate(0.1,0.9)
print(rn2)

# Generate a random integer between 1 and 10
rnn=random.choice(range(1,11))
# Ask the user to guess the number
guess=int(input("Guess a number between 1 and 10: "))
# Check if the guess is correct
if guess==rnn:
  print("You guessed correctly!")
else:
  print("You guessed incorrectly!")
  
