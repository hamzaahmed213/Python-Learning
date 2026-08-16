
import random

yourchoice = int(input("Choose One\n1.Rock\n2.Paper\n3.Scissor\n"))
compchoice = random.randint(1,3)
choices = {
      1 : "Rock",
      2 : "Paper",
      3 : "Scissor"
    }
print(f"You Choose {choices[yourchoice]}\nComputer Choose {choices[compchoice]}\n")
if(yourchoice==compchoice):
    print("Its a Draw")
else:
    if(yourchoice == 1 and compchoice ==3):
        print("You Won")
    elif(yourchoice==2 and compchoice==1):
                    print("You Won")
    elif(yourchoice==3 and compchoice==2):
        print("You Won")
    else:
          print("Computer Won")
