while True:
    try:
        number = int(input("Enter a number: "))
        print("Odwrotna liczba to", 1 /number)
    except ValueError:
        print ("to nie jest liczba całkowita")
    except ZeroDivisionError:
        print("Błąd dzielenia przez 0")
    except:
        print(" Coś poszło nie tak... ")
