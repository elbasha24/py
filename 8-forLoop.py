# example 1
name= "basha"
for l in name:
    print(f"the letter {l} is in postion {name.index(l)}")
# example 2
for i in range(0,10):
    if(i%2 ==0):
     print(f"the number {i} is even")
    else:
      print(f"the number {i} is odd")
#example 3 - nested loop
for k in range(0,10):
    for m in range(20,30):
        print(k,m)
# example 4
# 1. Basic for loop
for i in range(5):
    print(i)

# 2. Loop over items in a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 3. Loop with a custom step
for i in range(0, 10, 2):
    print(i)

# 4. Nested for loops
for i in range(3):
    for j in range(2):
        print(i, j)

# 5. Loop with else statement
for i in range(3):
    print(i)
else:
    print("Loop finished")

# 6. Loop over a string
for letter in "hello":
    print(letter)

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)
