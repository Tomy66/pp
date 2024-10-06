# 1 ćwiczenie
name = "Mateusz"
surname = "Mękarski"
age = "27"
city = "Kraków"

print("Imię:" + name + ".")
print("Nazwisko:" + surname + ".")
print("Wiek:" + age + ".")
print("Miasto:" + city + ".")

print()

# 2 ćwiczenie
# długości boków kwadratów
a = 2  # kwadrat 1
b = 7  # kwadrat 2
c = 11  # kwadrat 3
d = 19  # kwadrat 4

# pola powierzchni (bok do kwadratu)

print("Pole 1 kwadratu ma pole:", a ** 2)
print("Pole 2 kwadratu ma pole:", b ** 2)
print("Pole 3 kwadratu ma pole:", c ** 2)
print("Pole 4 kwadratu ma pole:", d ** 2)

print()
# Obwód (4*bok)

print("Obwód 1 kwadratu ma pole:", 4 * a)
print("Obwód 2 kwadratu ma pole:", 4 * b)
print("Obwód 3 kwadratu ma pole:", 4 * c)
print("Obwód 4 kwadratu ma pole:", 4 * d)

print()
# Długość przekątnej (2
print("Długość przekątnej 1 kwadratu ma pole:", round((a ** 2 + a ** 2) ** 0.5, 2))
print("Długość przekątnej 2 kwadratu ma pole:", round((b ** 2 + b ** 2) ** 0.5, 2))
print("Długość przekątnej 3 kwadratu ma pole:", round((c ** 2 + c ** 2) ** 0.5, 2))
print("Długość przekątnej 4 kwadratu ma pole:", round((d ** 2 + d ** 2) ** 0.5, 2))

print()

# 3 ćwiczenie

start_deposit = 46_567.
deposit = start_deposit
factor = 1.075

deposit *= factor
deposit *= factor
deposit *= factor

print("Zysk z inwestycji wynosi:", round(deposit - start_deposit, 2), "zł.")
