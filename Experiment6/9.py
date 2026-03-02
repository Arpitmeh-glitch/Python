def create_dict(list1, list2):
    result = {}
    for i in range(min(len(list1), len(list2))):
        result[list1[i]] = list2[i]
    return result

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

print(create_dict(list1, list2))