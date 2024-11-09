# Gra toczy się dopóki nie zostanie odgadnięta liczba

import random

counter = 1

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != number:
    guess = int(input("Nie, to nie ta. Spróbuj jeszcze raz: "))
    counter += 1
print("You guessed it right for " + str(counter) + " time.")