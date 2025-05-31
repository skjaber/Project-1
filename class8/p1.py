class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The {self.model} ({self.year}) engine has started."

my_car = Car("Toyota", 2020)
print(my_car.start_engine())
