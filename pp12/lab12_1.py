# Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie.

def print_char(char="*", repeat=10, vertical=False):
    for i in range(repeat):
        if vertical:
            print(char)
        else:
            print(char + " ", end="")
    if not vertical:
        print()
    print()

print_char()
print_char(char="?", repeat=3, vertical=False)
print_char(char="|", repeat=4, vertical=True)
print_char(char="$", repeat=5, vertical=True)