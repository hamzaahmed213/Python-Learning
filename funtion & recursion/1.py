def greatest(a,b,c):
    if(a>b and a>c):
        print(f"Greatest is {a}")
    elif(b>a and b>c):
        print(f"Greatest is {b}")
    elif(c>a and c>b):
        print(f"Greatest is {c}")
    else:
        print("All are Equal")

a = 10
b=12
c = 32
greatest(a,b,c)