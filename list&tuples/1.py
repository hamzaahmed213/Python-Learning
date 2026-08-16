#To store name of fruits enter by user in a list

fruits = []
i =1
while(i<6):
    fruits.append(input(f"Enter {i} Fruit Name: "))
    i+=1

else:
    print(f"Thank You \n Your list is\n {fruits}")

