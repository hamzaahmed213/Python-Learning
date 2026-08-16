def starmaking(n):
    if n == 0:
        return
    print ("*"*n)
    starmaking(n-1)

n = int(input("Enter A number: "))
starmaking(n)