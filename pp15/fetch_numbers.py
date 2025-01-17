numbers = []
counter = 1

while True:
    if counter > 5:
        break
    try:
        number = int(input("Podaj liczbę całkowtitą "))
        numbers.append(number)
        counter += 1
    except:
        print("To nie jest liczba całkowta")

print(numbers)
