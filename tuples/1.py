# Find the Largest Number
numbers = (15, 42, 89, 23, 89, 67, 54, 42)
i=0
largest = numbers[i]
lenght = len(numbers)
while(i<lenght):
    if(largest<numbers[i]):
        largest = numbers[i]

    i+=1

print(largest)
    
