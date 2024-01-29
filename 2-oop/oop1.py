class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Driving the {self.brand} {self.model}")

my_car = Car("Toyota", "Camry")
my_car.drive()
