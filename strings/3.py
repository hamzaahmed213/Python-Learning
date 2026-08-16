#write a program to detect double space in string

letter= "my  name is  hamza  ahmed"
count = letter.count("  ")
letter = letter.replace("  "," ")
print(letter)
print(count)