def fun(list1, list2):
    intersection = [value for value in list1 if value in list2]
    reunion = list(set(list1) | set(list2))
    
    uniquesFromList1 = []
    for num in list1:
        if num not in list2:
            uniquesFromList1.append(num)

    uniquesFromList2 = []
    for num in list2:
        if num not in list1:
            uniquesFromList2.append(num)

    return intersection, reunion, uniquesFromList1, uniquesFromList2
    
print(fun([1,2,3,4,7,9], [1,4,7,2]))

# [1,2,3,4,7,9]
# [1,4,7,2]