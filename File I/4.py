# Write a program to generate multiplication tables from 2 to 20 and write it to the different
# files. Place these files in a folder for a 13-year-old.

import os

os.mkdir("Tables")

for i in range(2,21):
    with open(f"Tables/table_{i}.txt","w") as file:
        for j in range (1,11):
            file.write(f"{i}x{j}={i*j}\n")
