# Zabezpiecz program zliczający punkty w grach (moduł 14, lab 3) przed
# wprowadzaniem błędnych danych przez użytkownika.


def fetch_and_validate(standard_msg, error_msg="To nie jest liczba"):
    while True:
        try:
            return int(input(standard_msg))
        except:
            print(error_msg)

def define_player(player_no):
    player_points = []
    player_name = input("Podaj imię {} gracza".format(player_no))
    return {player_name: player_points}


def define_players():
    players = {}
    players_total = fetch_and_validate("Podaj liczbę graczy (1-8): ")
    for i in range(players_total):
        players.update(define_player(i + 1))
    return players


def define_win_points():
    return fetch_and_validate("Zdefiniuj liczbę punktów wygranej: ")


def is_winer(players, win_points):
    for player in players.keys():
        if sum(players[player]) >= win_points:
            return True
        return False


def count_points(players, win_points):
    counter = 1
    while True:
        print("\nTura", counter)
        for player in players.keys():
            player_points = fetch_and_validate("Podaj punkty dla gracza - {}".format(player))
            players[player].append(player_points)
            if is_winer(players, win_points):
                return player
    counter += 1
    return "winner"


def show_results(players, winner):
    print("\nWygrał gracz o imieniu {}, brawo!:".format(winner))
    print()
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)

players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
show_results(players, winner)
