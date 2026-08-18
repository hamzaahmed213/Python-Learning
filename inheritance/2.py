# Create a parent class Person:

# name
# age

# Create a child class Student that additionally has:

# roll_no
# course

# Create a display() method in Student that prints all four values.

class person:
    name = "Hamza"
    age = 20

class student(person):
    roll_no = 'BTECH/IT/098'
    course = "BTECH"

    def display(self):
       
        print(self.name,self.age,self.roll_no,self.course)

s = student()
s.display()