# Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
# • zapytaj użytkownika o wzrost i wagę,
# • stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
# • stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
# otyłość) na podstawie wskaźnika BMI,
# • zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.

print("Obliczenie wskaźnika BMI!")

weight_in_kg = float(input("Podaj swoją wage (kg): "))
hight_in_cm = float(input("Podaj swój wzrost (cm): "))


def calculate_bmi(weight_in_kg, hight_in_m):
    return weight_in_kg / hight_in_m ** 2

def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"



bmi = calculate_bmi(weight_in_kg, hight_in_cm * .01)
category = determine_bmi_category(bmi)

print("Wskaźnik BMI: ", round(bmi, 2))
print("Kategoria: " , category)
