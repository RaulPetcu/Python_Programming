def uniqueAndNotUnique(list):
    unique_elements = set(list)
    duplacitie_elements = len(list) - len(unique_elements)

    return (unique_elements, duplacitie_elements)

print(uniqueAndNotUnique([1,2,1,1,1,1,2,2,3,4,4,5]))



