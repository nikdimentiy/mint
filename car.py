"""Class to provide a car layout"""


class Car():
    """"Simple car model"""

    def __init__(self, make, model, year):
        """Initializes the attributes of the car description"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a neatly formatted description"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Prints the car's mileage in miles"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Sets a given value on the odometer. When you try to cheat back, the changes are rejected"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increases odometer reading with a given increment"""
        self.odometer_reading += miles
