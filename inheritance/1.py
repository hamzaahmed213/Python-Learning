# Create a parent class Animal with:

# name
# method speak() that prints "Animal makes a sound"

# Create a child class Dog that inherits from Animal.

# The Dog should have its own method:

# bark()

# that prints "Dog barks".

# Create a Dog object and call both methods.

class animal:
    def speak(self):
        print("Animal Makes a sound")

class dog(animal):
    def bark(self):
        print("Dog Barks")

d = dog()
d.bark()
d.speak()