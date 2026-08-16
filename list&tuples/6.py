# Find Duplicate Elements
numbers = [10, 20, 30, 20, 40, 50, 10, 60, 30]
check = []
i = 0
while(i<len(numbers)):
    if(numbers.count(numbers[i])>1 and numbers[i] not in check):
        print(f"{numbers[i]} is a duplicate")
        check.append(numbers[i])
        
    i+=1