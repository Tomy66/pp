#Napisz grę polegającą na zapamiętywaniu kolejnych słów. Wylosowany
# gracz podaje pierwsze słowo a kolejny powtarza słowo i dodaje swoje.
# Następny w kolejce gracz musi podać wszystkie wcześniejsze słowa w tej
# samej kolejności i także dodać swoje. Rozgrywka kończy się gdy, któryś z
# graczy popełni błąd. Na ekranie komputera przy każdej turze należy
# wymazać ekran np. przez wyświetlenie 100 pustych wierszy.

import random

# Funkcja do wyczyszczenia ekranu
def clear_screen():
    print("\n" * 100)

# Inicjalizacja gry
num_players = int(input("Podaj liczbę graczy: "))
players = [input(f"Podaj nazwę gracza {i + 1}: ") for i in range(num_players)]

# Wybór losowego gracza do rozpoczęcia
current_player = random.randint(0, num_players - 1)
sequence = []  # Lista przechowująca ciąg słów

# Rozgrywka
while True:
    clear_screen()
    print(f"Tura gracza: {players[current_player]}")
    print("Powtórz dotychczasowe słowa w poprawnej kolejności i dodaj nowe.")

    # Pobranie odpowiedzi gracza
    response = input("Twoja odpowiedź: ").split()

    # Sprawdzenie poprawności
    if response[:len(sequence)] != sequence:
        print(f"Błąd! {players[current_player]} podał złą sekwencję.")
        winner = players[current_player - 1] if current_player > 0 else players[-1]
        print(f"Zwycięzcą jest: {winner}")
        break

    # Dodanie nowego słowa
    if len(response) > len(sequence):
        sequence.append(response[-1])
    else:
        print(f"{players[current_player]} nie dodał nowego słowa. Koniec gry.")
        winner = players[current_player - 1] if current_player > 0 else players[-1]
        print(f"Zwycięzcą jest: {winner}")
        break

    # Zmiana gracza
    current_player = (current_player + 1) % num_players