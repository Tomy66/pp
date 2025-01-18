from lotto import get_user_numbers, draw_numbers, check_numbers

print("Witaj w grze lotto!")
user_numbers = get_user_numbers()
print("Pobrane liczby to:", user_numbers)

input("\nNaciśnij enter aby dokonać losowania liczb\n")
input()
lucky_numbers = draw_numbers()
print("Wylosowano liczby:", lucky_numbers)
print()

result = check_numbers(user_numbers, lucky_numbers)
if result == 6:
    print("Gratulacje! Jesteś milionerem")
elif result == 5:
    print("Brawo! Trafiłeś piątke")
elif result == 4:
    print("Hura! Tradfiono czwórke")
elif result == 3:
    print("Trafiono trójkę, przysługuje Ci minimalna wygrana")
elif result == 2 or result == 1:
    print("Trafiono {} liczbę. Było bardzo blisko".format(result))
else:
    print("To nie jest Twój dzień")