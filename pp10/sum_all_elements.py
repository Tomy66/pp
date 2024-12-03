total = 0

numbers = [1,3,53,24,33,12,67,55]

for number in numbers:
    total += number

print("Suma wszystkich elementów list", numbers, "to", str(total) + ".")

print(sum(numbers))