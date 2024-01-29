
# Creating a Class and Object:
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Driving the {self.brand} {self.model}")

my_car = Car("Toyota", "Camry")
my_car.drive()

# Inheritance:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

my_dog = Dog("Buddy")
my_dog.speak()


# Encapsulation

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

my_account = BankAccount("123456789", 1000)
print(my_account.get_balance())
my_account.withdraw(500)
print(my_account.get_balance())


# Polymorphism

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())

# Class Method:

class MathUtils:
    @classmethod
    def add(cls, x, y):
        return x + y

result = MathUtils.add(5, 3)
print(result)

