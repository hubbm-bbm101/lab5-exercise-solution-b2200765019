email = input("Please enter your e-mail.")
validChar = 0
while True:
    for index in email:
        if index == "@" or index == ".":
            validChar += 1
    if validChar == 2:
        print("Thank you")
        break
    else:
        validChar = 0
        email = input("Please enter valid e-mail.")

