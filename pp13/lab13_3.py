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


