#Korzystając z odpowiednich modułów napisz skrypt realizujący następujące
# zadania:
# • wyświetl informacje o procesorze komputera,
# • wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
# • wyznacz sinus 90 stopni.

import platform
import random
import math

print(platform.machine())
print(random.sample(range(1,10), 3))
print(math.sin(math.radians(90)))