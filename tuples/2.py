# Find the Smallest Number
numbers = (45, 12, 78, 3, 56, 19, 8, 99)
smallest = numbers[0]
i = 0
while i<len(numbers):
    if smallest > numbers[i]:
        smallest = numbers[i]
    i+=1

print(f"Smallest is {smallest}")