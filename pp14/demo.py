# numbers = (1, 2, 3, 4, 5)
#
# for number in numbers:
#     print(number)
#
# numbers = tuple(x for x in range(10) if x % 2 == 0)
# # print(numbers)

# numbers =(1,2,3)
# print(len(numbers))
# print(numbers*2)
# print(numbers + numbers)

# numbers = [1,2,3]
# print(numbers, type(numbers))
# numbers = tuple(numbers)
# print(numbers)

# letters = tuple("Ala lalalal")
# print(letters)


#SŁOWNIKI

# phones = {"Kita": 12345678, "Ada": 987654, "Ola": 6543217654}
# print(phones)

animals_dict ={
    "kot":"cat",
    "pies": "dog",
    "ptak": "bird"
}
#
# print(animals_dict["kot"])
# print(animals_dict.get("ptak"))
# print(animals_dict.get("chomik", "Brak takiego klucza w słowniku"))
# print(animals_dict.get("pies", "Brak takiego klucza w słowniku"))

# words = ["kot", "lew", "chomik"]
#
# for word in words:
#     if word in animals_dict.keys():
#         print(word, "->", animals_dict[word])
#     else:
#         print("Nie znaleziono słowa {} w słowniku".format(word))

# for key in animals_dict:
#     print(key, "->", animals_dict[key])
#
# print()
#
# for value in animals_dict.values():
#     print(value)
#
# print()
#
# for item in animals_dict.values():
#     print(item)
#
# print()
#
# for pl, en in animals_dict.items():
#     print(pl, "->", en)
#
# print()

animals_dict["świnka"]="pig"
print(animals_dict)
print(animals_dict.popitem())
print(animals_dict)