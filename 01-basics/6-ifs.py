# if statment in python

def is_leap(year):
    """Checks whether a year is a leap year or not."""
    if (year % 4 == 0 and year % 100 != 0
        or year % 400 == 0):
        return True
    else:
        return False

print("Is the year 2000 a leap year?", is_leap(2000))

print("Testing the is_leap function:")
print("Is the year 2001 a leap year?", is_leap(2001))

# name=input("enter your name: ")
# if(name == "Nasr"):
#     print("Hello Nasr!")
# elif(name == "Mohamed"):
#     print("Hello Mohamed")
# else:
#     print("Hello Guest!")

name=input("enter your name: ")
if(name == "Nasr"):
    print(f"Your name is {name} and has {len(name)} letters ")
elif(name == "Mohamed"):
    print(f"Your are not Nasr and your name is {name} which has {len(name)} letters ")
else:
   print(f"Your are a guest and your name {name} has {len(name)} letters ")
