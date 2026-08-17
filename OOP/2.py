# College Students

# Create a Student class where:

# Every student has a different name and roll
# Every student belongs to the same college
# The college name should be stored as a class attribute

class student: 
    college_name = "MCKV Institute of Technology"
  

hamza = student()
hamza.name = "Hamza"
hamza.roll = 20

aditya = student()
aditya.name= "aditya"
aditya.roll = 23

print(hamza.name, hamza.roll, hamza.college_name)
print(aditya.name, aditya.roll, aditya.college_name)
