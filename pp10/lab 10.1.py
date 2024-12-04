names = []

total_elements = int(input("Podaj liczbę imion jakie zamierzasz wprowadzić: "))
for i in range(total_elements):
    names.append(input("Podaj" + str(i+1)+ "imię: "))

print("Od użytkownia pobrano następujące imiona:", names)
