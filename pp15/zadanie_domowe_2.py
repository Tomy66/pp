# Chcemy ułożyć wieżę z puszek. Wieża składa się z poziomów, gdzie każdy
# wyższy poziom wymaga jednej puszki mniej niż poziom na którym go
# zbudowano. Korzystając z rekurencji napisz program, który pozwoli
# wyliczyć ilość potrzebnych puszek do wybudowania wieży o zadanym
# poziomie oraz ilość poziomów wieży jakie jesteśmy wstanie ułożyć z
# dostępnej liczby puszek. Przykład: jeżeli chcemy ułożyć 3 poziomową
# wieżę potrzebujemy 6 puszek a np. mając 10 puszek, ułożymy 4
# poziomową wieżę.

def puszki_na_wieze(poziom):
    """Oblicza liczbę puszek potrzebnych do zbudowania wieży o danym poziomie."""
    if poziom == 1:
        return 1
    return poziom + puszki_na_wieze(poziom - 1)

def maksymalny_poziom(puszki, poziom=1):
    """Oblicza maksymalną liczbę poziomów wieży, które można ułożyć z dostępnej liczby puszek."""
    if puszki < poziom:
        return poziom - 1
    return maksymalny_poziom(puszki - poziom, poziom + 1)

# Przykład użycia
poziom_wiezy = 3
liczba_puszek = 10

# Obliczenie puszek potrzebnych na określony poziom
puszki_potrzebne = puszki_na_wieze(poziom_wiezy)
print(f"Aby ułożyć {poziom_wiezy}-poziomową wieżę, potrzebujemy {puszki_potrzebne} puszek.")

# Obliczenie maksymalnego poziomu wieży dla danej liczby puszek
maks_poziom = maksymalny_poziom(liczba_puszek)
print(f"Z {liczba_puszek} puszek można ułożyć {maks_poziom}-poziomową wieżę.")
