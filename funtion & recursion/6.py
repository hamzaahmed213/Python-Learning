def table(i,n):
    
    if i ==11:
        return
    print(f"{n}x{i}={n*i}")
    table(i+1,n)

n = int(input("Enter A Number"))
i = 1
table(i,n)
