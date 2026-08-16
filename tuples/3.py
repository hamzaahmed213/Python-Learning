# Hard – Find the Second Largest Number
numbers = (15, 42, 89, 23, 89, 67, 54, 42)
largest = numbers[0]
second_largest = numbers[0]
i = 0;
while(i<len(numbers)):
    if largest<numbers[i]:
        largest = numbers[i]
        if second_largest>numbers[i] and second_largest<largest:
            second_largest = numbers[i]

    i+=1

print(second_largest)

wrong