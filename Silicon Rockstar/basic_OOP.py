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
        return long_name

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
# print(my_car.year)
print(my_car.descriptive_name())
