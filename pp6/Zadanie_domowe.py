# 1 zadanie
print("*        *")
print("**      **")
print("***    ***")
print("****  ****")
print("**********")
print("****  ****")
print("***    ***")
print("**      **")
print("*        *")

print()

# 2 zadanie
# Rozmiar pliku testowego i czas pobrania
file_size_mb = 194  # MB
download_time_seconds = 5  # sekundy

# Obliczenie prędkości pobierania w MB/s
download_speed = file_size_mb / download_time_seconds

# Rozmiar danych do pobrania w TB i przeliczenie na MB
total_size_tb = 13  # TB
total_size_mb = total_size_tb * 1024 * 1024  # konwersja TB na MB

# Obliczenie czasu pobierania w sekundach
total_time_seconds = total_size_mb / download_speed

# Konwersja czasu na godziny
total_time_hours = total_time_seconds / 3600

# Zaokrąglenie do pełnych godzin
total_time_hours_rounded = round(total_time_hours)

print(f"Czas potrzebny na pobranie 13 TB danych: {total_time_hours_rounded} godzin")
print()

# 3 zadanie

bank_account=30_000.
deposit_1 = bank_account
deposit_2 = bank_account
deposit_3 = bank_account
factor_1= 0.075
factor_2= 0.08
factor_3= 0.0825

# Saldo po pierwszym kwartale - Wariant I
deposit_1*=1+(factor_1/4)
print("Saldo po pierwszym kwartale przy oprocentowaniu 7,5% wynosi", round(deposit_1,2))
# Saldo po drugim kwartale - Wariant I
deposit_1*=1+(factor_1/4)
print("Saldo po drugim kwartale przy oprocentowaniu 7,5% wynosi", round(deposit_1,2))
#Saldo po trzecim kwartale - Wariant I
deposit_1*=1+(factor_1/4)
print("Saldo po trzecim kwartale przy oprocentowaniu 7,5% wynosi", round(deposit_1,2))
#Saldo po czwartym kwartale - Wariant I
deposit_1*=1+(factor_1/4)
print("Saldo po czwartym kwartale przy oprocentowaniu 7,5% wynosi", round(deposit_1,2))
print()
print("Roczny zysk z inwestycji przy oprocentowaniu 7,5% wynosi", round(deposit_1-bank_account,2))
print()

#Saldo po pierwszym kwartale - Wariant II
deposit_2*=1+(factor_2/4)
print("Saldo po pierwszym kwartale przy oprocentowaniu 8% wynosi", round(deposit_2,2))
#Saldo po drugim kwartale- Wariant II
deposit_2*=1+(factor_2/4)
print("Saldo po drugim kwartale przy oprocentowaniu 8% wynosi", round(deposit_2,2))
#Saldo po trzecim kwartale - Wariant II
deposit_2*=1+(factor_2/4)
print("Saldo po trzecim kwartale przy oprocentowaniu 8% wynosi", round(deposit_2,2))
#Saldo po czwartym kwartale - Wariant II
deposit_2*=1+(factor_2/4)
print("Saldo po czwartym kwartale przy oprocentowaniu 8% wynosi", round(deposit_2,2))
print()
print("Roczny zysk z inwestycji przy oprocentowaniu 8% wynosi", round(deposit_2-bank_account,2))
print()

#Saldo po pierwszym kwartale - Wariant III
deposit_3*=1+(factor_3/4)
print("Saldo po pierwszym kwartale przy oprocentowaniu 8,25% wynosi", round(deposit_3,2))
#Saldo po drugim kwartale - Wariant III
deposit_3*=1+(factor_3/4)
print("Saldo po drugim kwartale przy oprocentowaniu 8,25% wynosi", round(deposit_3,2))
#Saldo po trzecim kwartale - Wariant III
deposit_3*=1+(factor_3/4)
print("Saldo po trzecim kwartale przy oprocentowaniu 8,25% wynosi", round(deposit_3,2))
#Saldo po czwartym kwartale - Wariant III
deposit_3*=1+(factor_3/4)
print("Saldo po czwartym kwartale przy oprocentowaniu 8,25% wynosi", round(deposit_3,2))
print()
print("Roczny zysk z inwestycji przy oprocentowaniu 8,25% wynosi", round(deposit_3-bank_account,2))
