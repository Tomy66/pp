# skrypt pobiera liczbe od użytkownika
# wyświetla informacje czy dana liczba jest parzysta , podzielna przez 5 i 7

number = int(input("Enter a number: "))
print("Liczba jest: ")

if number % 2 == 0:
    print("Liczba jest parzysta")
else:
    print(" Liczba nieparzysta")

if number % 5 == 0:
    print("Liczba podzielna przez 5")
else:
    print("Liczba niepodzielna przez 5")

if number % 7 == 0:
    print("Liczba podzielna przez 7")
else:
    print("Liczba niepodzielna przez 7")