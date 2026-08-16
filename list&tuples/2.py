#accept 5 marks and show them in a sorted manner

marks = []
i=1
while(i<6):
    marks.append(int(input(f"Enter Student {i} Marks: ")))
    i+=1
else:
    marks.sort()
    print(f"Thanks\nHeres List in Sorted Manner\n{marks}")