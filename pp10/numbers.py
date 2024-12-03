#wylosuj 10 dowolnych licz od 1 do 100
#umieść w liście
#wyświetl liste

import random

numbers = []
for i in range(10):
    number = random.randint(1, 100)
    numbers.append(number)
print(numbers)

fruits = ['apple','plum','banana']
for i in range(len(fruits)):
    print(fruits[i])

print()

for fruit in fruits:
    print(fruit)