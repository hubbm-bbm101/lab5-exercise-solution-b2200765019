import random
number = random.randint(0,100)
while True:
    guess = int(input("Enter a number:"))
    if guess > number:
        print("Decrease your number")
    elif guess < number:
        print("Increase your number")
    else:
        print("Correct guess. Congratulations!")
        break