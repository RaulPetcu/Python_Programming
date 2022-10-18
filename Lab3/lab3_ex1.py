def setOperation(list1, list2):
    result = []
    intersection = {}
    intersection = list(set(list1) & set(list2))

    reunion = set()
    reunion = list(set(list1) | set(list2))

    uniquesFromList1 = set()
    for el in list1:
        if el not in list2:
            uniquesFromList1.add(el)

    uniquesFromList2 = set()
    for el in list2:
        if el not in list1:
            uniquesFromList2.add(el)

    result.append(intersection)
    result.append(reunion)
    result.append(uniquesFromList1)
    result.append(uniquesFromList2)


    return result

print(setOperation([1,23,4,54,1,3], [43,54,6,123,3]))