temp = 12
is_sun_shining = False

#Jeżeli będzie dodatnia temp i bd słonecznie to....
#pójdziemy na spacer a jeżeli nie to zostaniemy w domu
if temp > 0 and is_sun_shining:
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")

print("-" *20)

#Jeżeli będzie ujemna temperatura lub będzie pochmurnie to...
#zostaniemy w domu a jeżeli nie to pójdziemy na spacer

if not (temp < 0 or not is_sun_shining):
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")

print()
#operatory logiczne
# and - koniunkcja - czytamy jak i
# or - alternatywa - czytamy jak lub
# not - negacja - czytamy jak nie

#iterujemy od 0-9 (10 iteracji)
#wyświetlamy cyfrę chyba, że...
#liczba parzysta lub liczba większa od 6 to wyświetl *

for i in range(10):
    if i % 2 == 0 or i > 6:
        print("*")
    else:
        print(i)

print()

a,b,c = 2,3,4
if a <b and b< c:
    print("!!!")

a = 5
b = 3

#koniunkcja bitowa
print(a, "&", b, "=", a & b)
print("{:08b}". format(a))
print("{:08b}". format(b))
print("-" * 8)
print("{:08b}". format(a & b))
print()

#alternatywa bitowa
print(a, "|", b, "=", a | b)
print("{:08b}". format(a))
print("{:08b}". format(b))
print("-" * 8)
print("{:08b}". format(a | b))
print()

#alternatywa rozłączna bitowa
print(a, "^", b, "=", a ^ b)
print("{:08b}". format(a))
print("{:08b}". format(b))
print("-" * 8)
print("{:08b}". format(a ^ b))
print()

#przesunięcie bitowe w prawo
print(a, ">>", b, "=", a >> b)
print("{:08b}". format(a))
print("-" * 8)
print("{:08b}". format(a >> b))
print()

#przesunięcie bitowe w lewo
print(a, "<<", b, "=", a << b)
print("{:08b}". format(a))
print("-" * 8)
print("{:08b}". format(a << b))
print()

#negacja bitowa
print("~" + str(a), "=", ~ a)
print("{:08b}". format(a))
print("-" * 8)
print("{:08b}". format(~a))
print()

#00000010 ()
#00000001 (1)
#00000000 (0)
#11111111 (-1)
#11111110 (-2)

# for i in range(5,-6, -1):
#     print("{0:08b} => {1:d}" .format(*args: i & 255, i))

