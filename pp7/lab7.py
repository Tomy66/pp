# Zadanie 1
number = int(input("Enter a number: "))
if number ** (1/2) % 1 == 0:
    print("Liczba jest całkowita")
else:
    print(" Liczba nie jest całkowita")


#Zadanie 2

points = int(input("Enter a number of points (1-100):"))
if points >= 95:
    print("Uzyskałeś ocenę 5.0")
elif points < 95 and points >=84:
    print("Uzyskałeś ocenę 4.5")
elif points < 84 and points >=70:
    print("Uzyskałeś ocenę 4.0")
elif points < 70 and points >=60:
    print("Uzyskałeś ocenę 3.5")
elif points < 60 and points >=50:
    print("Uzyskałeś ocenę 3.0")
else:
    print("Uzyskałeś ocene 2.0")





#Zadanie 3
import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congrats! That's the number!")
elif guess > number:
    print("Sorry, that's not correct. Try again, the number is lower. You have 2 more chances.")
elif guess < number:
    print("Sorry, that's not correct. Try again, the number is higher. You have 2 more chances.")

guess = int(input("Guess a number between 1 and 10: "))
if guess == number:
    print("Congrats! That's the number!")
elif guess > number:
    print("Sorry, that's not correct. Try again, the number is lower. You have 1 more chances.")
elif guess < number:
    print("Sorry, that's not correct. Try again, the number is higher. You have 1 more chances.")

guess = int(input("Guess a number between 1 and 10: "))
if guess == number:
    print("Congrats! That's the number!")
elif guess > number:
    print("Sorry, that's not correct. Try again, the number is lower. You lose")
elif guess < number:
    print("Sorry, that's not correct. Try again, the number is higher. You lose")

#Zadanie 3 Wersja 2

import random

number= random.randint(1, 10)
msg = "Guess a number between 1 and 10: "
guess = int(input(msg))

if guess == number:
    print("Congrats! That's the number!")
else:
    msg ="Masz kolejną szanse "
    if number%2 == 0:
        msg+= "parzysta: "
    else:
        msg += "nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Congrats! That's the number!")
    else:
        msg = "masz ostatnią szanse, moja liczba jest "
        if number > 5:
            msg += "większa niż "
        else:
            msg += "mniejsza lub równa"
        msg += "pięć: "
        guess = int(input(msg))
        if guess == number:
            print("Congrats! That's the number!")
        else:
            print("niestety, myślałem o liczbie " + str(number) + ".")