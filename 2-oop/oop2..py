# create class
class Person:
    # create constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #  method to display details of person and access the constructor objects.
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
person = Person("John", 30)
person.greet()


