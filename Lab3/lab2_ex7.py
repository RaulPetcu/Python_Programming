from numpy import intersect1d


def setOperation(set1, set2):
    result = []
    intersection = []
    intersection = list(set(set1) & set(set2))

    reunion = []
    reunion = list(set(set1) | set(set2))

    uniquesFromSet1 = []
    for el in set1:
        if el not in set2:
            uniquesFromSet1.append(el)

    uniquesFromSet2 = []
    for el in set2:
        if el not in set1:
            uniquesFromSet2.append(el)

    result.append(len(reunion))
    result.append(len(intersection))
    result.append(len(uniquesFromSet1))
    result.append(len(uniquesFromSet2))

    return result


def dict_operations(*argv):
    dict = {}

    list_of_sets = []
    for set in argv:
        list_of_sets.append(set)
    
    for i in range(len(list_of_sets)):
        for j in range(i+1, len(list_of_sets)):
            # fac operatii intre seturile list_of_sets[i] si list_of_sets[j]
            set1 = list_of_sets[i]
            set2 = list_of_sets[j]
            operation_results = setOperation(set1, set2)

            reunion = str(set1) + " | " + str(set2)
            dict[reunion] = operation_results[0]

            intersection = str(set1) + " & " + str(set2)
            dict[intersection] = operation_results[1]

            uniqueFromSet1 = str(set1) + " - " + str(set2)
            dict[uniqueFromSet1] = operation_results[2]

            uniqueFromSet2 = str(set2) + " - " + str(set1)
            dict[uniqueFromSet2] = operation_results[3]

    return dict


print(dict_operations({1,2}, {2,3}))
            
