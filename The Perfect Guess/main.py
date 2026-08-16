# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please” .
# Similarly, if the user’s guess is too low, the program prints “Higher number please” .
# When the user guesses the correct number, the program displays the number of
# guesses the player used to arrive at the number.

import random

comp_n = random.randint(1,10)

guesses = 0

while True:

    n = int(input("Enter A Number Between 1 to 10:"))
    guesses +=1
    if comp_n == n:
        print(f"You Won!\nTotal Guesses Took {guesses}\nComputer choose {comp_n} and you choose {n}")
        break
    else:
        if n > comp_n:
            print("Lower Number")
        else:
            print("Higher Number")
    print(f"Guess Count:{guesses}")