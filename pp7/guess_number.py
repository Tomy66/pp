import random

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
print(number)

if guess == number:
    print("Congrats! That's the number!")
else:
    print("Sorry, that's not correct.")