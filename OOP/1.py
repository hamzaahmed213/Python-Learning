# 1. Student Class

# Create a Student class that stores:

# name
# age
# course

# Create 3 student objects with different values and print their details.

class student:

    name = "hamza"
    age = 20
    course = "BTECH"

    def __init__(self,name,age,course):
        self.name = name 
        self.age = age 
        self.course = course 

        print(f"Name is {name}, Age is {age} and Course is {course}")

hamza = student("Hamza", 20, "BTECH")
aditya = student("Aditya", 23, "BTECH")
Athar_Jamil = student("Athar Jamil", 21, "BCA")