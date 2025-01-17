# Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informację o jego braku.

phones = {"Kita": 12345678, "Ada": 987654, "Ola": 6543217654}

# name = input("Enter your name: ")
# for name in phones:
#     if name in phones.keys():
#         print(name, "->", phones[name])
#     else:
#         print("Nie znaleziono słowa {} w słowniku".format(name))

def get_number():
    while True:
        name = input("Enter name: ")
        if name == "":
            break
        if name in phones.keys():
            print(name, "->", phones[name])
        else:
            print("Nie znaleziono słowa {} w słowniku".format(name))

print(get_number())