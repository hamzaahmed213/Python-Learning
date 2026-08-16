# Count Even and Odd Numbers
numbers = [12, 15, 7, 20, 33, 44, 19, 50]

i = 0
lenght = len(numbers)
while(i<lenght):
    if(numbers[i]%2==0):
        print(f"{numbers[i]} is even")
    else:
        print(f"{numbers[i]} is odd")

    i+=1