# Create a parent class Vehicle with:

# brand
# speed

# and a method:
# display()

# Create a child class Car that additionally has:
# number_of_doors

# Override the display() method in Car so it prints:
# Brand: Toyota
# Speed: 120
# Doors: 4

class vehicle:
    brand = "Mercedes-Benz"
    model = "Maybach"

    def display(self):
        print(f"Brand:{self.brand}\nModel:{self.model}")

class car(vehicle):
    speed = 150
    number_of_doors = 4
    def display(self):
        super().display()
        print(f"Speed:{self.speed}\nDoors:{self.number_of_doors}")

c = car()
c.display()

    