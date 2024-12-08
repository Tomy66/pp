# Zadanie 1
#Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskaznej listy

#1 sposób
def pow(numbers, exponent):
    numbers = numbers[:] #zabezpieczenie przed modyfikacją listy
    for i in range(len(numbers)):
        numbers[i] = numbers[i]**exponent
    return numbers

numbers =[1,2,3]
print(pow(numbers,4))

#2sposób
def pow2(numbers, exponent):
    result =[]
    for n in numbers:
        result.append(n**exponent)
        return result

print(pow2(numbers,4))
