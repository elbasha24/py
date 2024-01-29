# function in python
# def add(a,b):
#     return (a+b)
# print(f"The sum of your nums is {add(12,13)}")

def add2(a, b):

    if a % 2 == 0 and b % 2 == 0:
        return (f"Both numbers are even and the total is {a+b}")
    elif a % 2 == 0 or b % 2 == 0:
        return (f"One number is even. and the sum {a+b}")
    else:
        return (f"Neither number is even. and the sum {a+b}")

print(add2(12, 30))
