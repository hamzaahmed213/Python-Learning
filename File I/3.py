with open("word.txt", "r") as file:
    data = file.readlines()

longest = data[0]
i = 0;
while(i<len(data)):
    if  len(data[i]) > len(longest):
        longest = data[i]
    i+=1
        

print(f"Longest is: {longest}and lenght is {len(longest) - 1}")