
def merge_lists_without_duplicates(source, target):
    for element in source:
        if element not in target:
            target.append(element)


def transform_data(list1, list2, list3):
    resoult = []
    merge_lists_without_duplicates(list1, resoult)
    merge_lists_without_duplicates(list2, resoult)
    merge_lists_without_duplicates(list3, resoult)
    return tuple(resoult)

print(transform_data([1,2],[1,1],[4,4,4]))
print(transform_data([1,2,3],[1,2,3],[4,5,6]))
print(transform_data(["Ala","ma"],["Ala", "ma", "kota"],["mysz"]))