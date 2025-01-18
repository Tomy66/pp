# Zmodyfikuj moduł lotto, aby dawał możliwość grania systemem tj. pozwalał
# skreślać od 6 do 12 liczb.

import random


def draw_numbers():
    numbers = [i for i in range(1, 50)]
    lucky_numbers = random.sample(numbers, 6)
    return lucky_numbers


def get_game_system():
    while True:
        try:
            number = int(input("Podaj ile liczb chcesz skreślić (6-12): "))
            if number < 6 or number > 12:
                print("Należy podać liczbę z przedziału 6-12")
                continue
            break
        except ValueError:
            print("To nie jest liczba")
            continue
    return number


def get_user_numbers():
    n = get_game_system()
    counter = 1
    user_numbers = []
    while counter <= n:
        try:
            number = int(input("Podaj {} liczbę (1-49): ".format(counter)))
            if number in user_numbers:
                print("Powtórzona liczba!")
                continue
            if number < 1 or number > 49:
                print("Należy podać liczbę z przedziału 1-49!")
                continue

        except:
            print("To nie jest liczba")
            continue
        user_numbers.append(number)
        counter += 1
    user_numbers.sort()
    return user_numbers


def check_numbers(user_numbers, lucky_numbers):
    counter = 0
    for number in user_numbers:
        if number in lucky_numbers:
            counter += 1
    return counter


if __name__ == '__main__':
    user_numbers = get_user_numbers()
    lucky_numbers = draw_numbers()
    result = check_numbers(user_numbers, lucky_numbers)
    print(user_numbers)
    print(lucky_numbers)
    print(result)
