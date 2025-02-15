#Napisz skrypt znajdujący wszyskie liczby z pzedziały od 100 do 300, które dzielą się jednocześnie przez 5 i 8.

for liczba in range(100,301):
    if liczba % 5 == 0 and liczba % 3 == 0:
        print(liczba)