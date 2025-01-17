# Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
# w tym celu:
# • za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
# • kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
# • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
# • przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter.

import random

FIRST_SYMBOL = 'A'
LAST_SYMBOL = 'H'
NUMBER_OF_LETTERS = 6

def draw_letter():
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL)))

def draw_row():
    return [draw_letter() for _ in range(NUMBER_OF_LETTERS)]

def check(row):
    first_element = row[0]
    for element in row:
        if first_element != element:
            return False
        return True

counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1


