# 1 Zadanie

import random

user_numbers = []
random_numbers = []
hit_total = 0

for i in range(6):
    user_numbers.append(int(input("Podaj " + str(i + 1) + " liczbę od 1 do 49: ")))


random_numbers= random.sample(range (1,50), 6) #bez powtórzeń

for number in user_numbers:
    if number in random_numbers:
        hit_total += 1

random_numbers.sort()
user_numbers.sort()

print(random_numbers)
print(user_numbers)
print("Trafiono", hit_total, "liczb.")
