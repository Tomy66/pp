# Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.

def remove_duplicates(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    return result

my_list = [1,1,3,4,3,5,6,5]
random_list = remove_duplicates(my_list)
print(random_list)