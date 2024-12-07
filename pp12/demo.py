name = input("Enter your name: ")
print("Witaj {}!".format(name))



##
def introduce(first_name, last_name):
    print("Cześć, jestem", first_name, last_name + ".")

introduce("Mateusz", "Mękarski")


##
def show_name(name="Jan"):
    print("Część mam na imię {}.".format(name))

show_name()

##
def empty_function():
    None
    2+2
    return 3

if empty_function() is None: #is None, ==None, is not None, !=None
    print("Funkcja nic nie zwróciła")