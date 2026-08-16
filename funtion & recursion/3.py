# Write a recursive function countdown(n) that prints numbers from n down to 1.

def countdown(n):
    if n == 0:
        return 
    print(n)
    countdown(n-1)

n = int(input("Enter A number"))
countdown(n )