name = input("Enter Your name: ")
date = input("Enter Todays date: ")
letter = '''
Dear name
your are selected
date
'''
letter = letter.replace("name", name)
letter = letter.replace("date", str(date))

print(letter)
