#Napisz program, który wyświetla na ekranie prostokąt o wymiarach 50x5

szerokosc = 50
wysokosc = 5

for i in range(wysokosc):
    if i == 0 or i == wysokosc-1:
        print("*" * szerokosc)
    else:
        print("*" + " " * (szerokosc - 2) + "*")