# Napisz skrypt znajdujący wszystkie liczby z przedziału 100 do 300,
# które dzielą się jednocześnie przez 5 i 8


for i in range(100, 300):
    if i % 5 == 0 and i % 8 == 0:
        print(i)
