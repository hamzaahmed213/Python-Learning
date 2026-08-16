# Write a recursive function factorial(n) that calculates the factorial of a number.

def factorical(n):
    if n == 1 or n == 0:
        return 1
    return n * factorical(n-1)

n = int(input("Enter A number: "))
print(f"Factorial is {factorical(n)}")