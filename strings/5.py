# Email Validator (Basic)

email = input("Enter Your Email: ")
countadd = email.count("@")

if countadd == 1 and "." in email:
    print("valid Email")

else:
    print("Not a valid email")