# Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
# prostokątów o następujących długościach boków:
# • 4 i 5,
# • 2678 i 5678,
# • 344555 i 788998.

def perimeter(a, b):
    return 2 * a + 2 * b


def surface_area(a, b):
    return a * b


def diagonal_length(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def show_result(a,b):
    print("Prostokąt o bokach {} i {}:".format(a,b))
    print("Obwód:", perimeter(a,b))
    print("Pole powierzchni:", surface_area(a, b))
    print("Długość przekątnek:", diagonal_length(a, b))
    print()

show_result(4,5)
show_result(2678,5678)
show_result(344555,788988)