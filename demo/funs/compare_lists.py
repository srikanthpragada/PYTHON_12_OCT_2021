def compare_lists(list1, list2):
    diff = set(list1) ^ set(list2)
    return len(diff) == 0


print(compare_lists([1, 2, 3], [2, 3, 1]))
print(compare_lists([1, 2, 4, 3], [2, 3, 1]))
print(compare_lists([1, 2, 2, 3], [2, 3, 1]))