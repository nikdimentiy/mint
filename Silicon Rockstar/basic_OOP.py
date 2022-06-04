class Car:
    """ Simple model of car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        """ Return format description"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """ Read odometer value"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """ Set (update) current value in odometer"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_car = Car("audi", "a5", 2021)


# print(my_car.make)
# print(my_car.model)
# # print(my_car.year)
# print(my_car.descriptive_name())

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 85

    def describe_battery(self):
        """ Show information about battery in car"""
        print("This car has a " + str(self.battery_size) + " kWh battery.")


my_tesla = ElectricCar("Tesla", "Model S", 2020)
print(my_tesla.descriptive_name())
my_tesla.describe_battery()

