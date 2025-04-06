"""
car_pretty_print.py
by Paul Renaud
4/6/2025
IvyTech SDEV220

This simple program creates a Vehicle class and an Automobile subclass. It then asks for information for a car,
and then displays that information.

"""

class Vehicle:
    v_type = "" # vehicle type, such as car, truck, plane, boat, broomstick, etc.

class Automobile(Vehicle):
    year = None
    make = None
    model = None
    doors = None  # 2 or 4
    roof_type = None  # solid or sunroof

    def __init__(self, year=None, make=None, model=None, doors=None, roof_type=None):
        """Creates a vehicle of type car. Every other field is optional, and can be entered by name,
        or in order: year (int), make, model, doors (int), roof_type."""
        self.v_type = "car"
        if year != None: self.year = year
        if make != None: self.make = make
        if model != None: self.model = model
        if doors != None: self.doors = doors
        if roof_type != None: self.roof_type = roof_type

    
    def __str__(self):
        """Returns vehicle information on separate lines. Any values that are None or empty will be supressed.
        """
        output_string = ""
        if self.v_type: output_string += " Vehicle type: " + self.v_type
        if self.year: output_string += "\n Year: " + str(self.year)
        if self.make: output_string += "\n Make: " + self.make
        if self.model: output_string += "\n Model: " + self.model
        if self.doors: output_string += "\n Number of doors: " + str(self.doors)
        if self.roof_type: output_string += "\n Type of roof: " + self.roof_type
        return output_string
    

car = Automobile()
print("\nEnter new information for a car")
print(" Vehicle type: " + car.v_type)
while True:
    try:
        car.year = int(input(" Enter vehicle year: "))
        break
    except:
        print("Please enter a valid year. Try again.")
car.make = input(" Enter vehicle make: ")
car.model = input(" Enter vehicle model: ")
while True:
    try:
        car.doors = int(input(" Enter number of doors: "))
        break
    except:
        print("Please enter a valid number. Try again.")
car.roof_type = input(" Enter vehicle roof type (solid or sunroof): ")

print("\nGot it! Here is the information I have.")
print(car)
