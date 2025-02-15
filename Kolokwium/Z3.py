#Pobierz od użytkownika trzy liczby całkowite reprezentujące długości odcinków i sprawdź czy jest możliwe zbudowanie z tch odcinków dowolnego trójkąta

a= int(input("Podaj pierwszą długośc odcinka: "))
b= int(input("Podaj drugą długośc odcinka: "))
c= int(input("Podaj trzecią długośc odcinka: "))

if a + b > c and a + c > b and b + c > a:
    print("Z podanych odcinków można zbudować trójkąt")
else:
    print ("Z podanych odcinków nie można zbudować trójkąta")