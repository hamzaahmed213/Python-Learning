# A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.

with open("donkey.txt","r") as file:
    data = file.read()

data = data.replace("donkey", "#####")

with open("donkey.txt","w") as file:
    file.write(data)