# Calculator

# Create a Calculator class with:

# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)

# Then make these methods static methods.

class calculator():

    @staticmethod
    def add(a,b):
        sum = a + b
        print(f"Sum is {sum}")
    @staticmethod
    def substract(a,b):
        difference = a - b
        print(f"Difference is {difference}")
    @staticmethod
    def multiple(a,b):
        product = a*b
        print(f"Product is {product}")
    @staticmethod
    def divide(a,b):
        print(f"Divisible is {a/b}")

    
a = int(input("Enter First Number: "))
b = int(input("Enter second Number: "))

       
calculator.add(a,b)
calculator.substract(a,b) 
calculator.multiple(a,b)
calculator.divide(a,b)
        


