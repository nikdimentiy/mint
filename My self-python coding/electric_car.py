# this example of the code shows one of the principles of OOP (inheritance):
# how a class of heir is created from the parent class

class Car:
    """Simple car model"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represents aspects of the car specific to electric cars"""

    def __init__(self, make, model, year):
        """Initializes the attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Displays battery power information"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

mercedes = Car("Mercedes", "S500", 2019)
mercedes.odometer_reading = 155
print(mercedes.get_descriptive_name())
mercedes.update_odometer(300)
mercedes.increment_odometer(50)
mercedes.read_odometer())

