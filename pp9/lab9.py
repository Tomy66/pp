# 1. Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika.
# 2. Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
# parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
# przynajmniej dzielą się przez 9.
# 3. Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
# całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.


range_from=int(input("od: "))
range_to=int(input("do: "))

is_first = True

print("Liczby z zakresu od", range_from, "do", range_to, "podzielne przez 3,5 lub 7 to:", end=" ")
for i in range(range_from,range_to+1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        if not is_first:
            print(", ", end="")
        print(i, end=" ")
    is_first=False
print(".")



## 2. Udowdonij, że w zbiorze licz z zakresu 1-100, jest 11 liczb, które są parzyste i jednocześnie większe od 90, a gdy są nieparzyste to przynajmniej dzielą się przez 9

counter = 0
for i in range(1, 101):
    if (i % 2 ==0 and i >90) or (i% 2 != 0 and i % 9 == 0):
        counter +=1

print("Tak to prawda, takich liczb jest ", str(counter) + ".")



## 3. Napisz program wyznaczający wartości n-tego bitu dla dowolnej liczby całkowitej. Bit liczymy od 0, od najmniej znaczącego bitu.

number = int(input("Podaj lczbę: "))
n = int(input("Podaj nr bitu "))


mask = 1 <<n
result = number & mask
bit = int(bool(result))

print("Bit dla pozycji", n, "dla liczby", number, "wynosi", str(bit) + ".")

#sprawdzenie
print("{:08b}".format(number))
print("{:08b}".format(mask))
print("-" * 8)
print("{:08b}".format(result))