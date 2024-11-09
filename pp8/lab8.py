# 1 zadanie
for i in range(101):
    if i % 3 != 0:
        print(i)

print()

# 2 zadanie
a = int(input("Podaj rozmiar: "))
b = input("Podaj znak: ")

for i in range(a):
    for j in range(a):
        print(b, end=" ")
    print()

print()

# 3 zadanie

s = 0
for i in range(64):
    s += 2 ** i
print("Suma wszystkich ziaren na szachownicy: " + str(s))

#założenia: waga 1 ziarna to 0,4 mg -> 0,004g

#1kg = 1000g
#1t = 1000kg

tons = int(s * 0.0004 / 1000 / 1000)
print("To będzie tyle ton: ", tons)

#roczna produkcja przenicy na świecie to 782 mln ton
years = int(tons/ 782_000_000)
print("lata: ", years)

# pociąg może przetransportować 2200t
trains = int(tons / 2200)
print("pociągów: ", trains)