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
        """Sets a given value on the odometer. 
           When you try to cheat back, the changes are rejected"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increases odometer reading with a given increment"""
        self.odometer_reading += miles


class Battery():
    """Simple car battery model"""

    def __init__(self, battery_size=70):
        """Initialiation of battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Displays battery power information"""
        print("This car has a " + str(self.battery_size) + " -kWh battery.")

    def get_range(self):
        """Displays an approximate power reserve for the battery"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Represents aspects of the car - specific to electric cars"""

    def __init__(self, make, model, year):
        """Initialize the attributes of the super class, after for subclass"""
        super().__init__(make, model, year)
        self.battery = Battery()
