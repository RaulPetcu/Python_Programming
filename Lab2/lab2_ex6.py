def fun(*lists, x):
    freq = {}
    newList = []
    for i in lists:
        for j in i:
            if j in freq:
                freq[j] += 1
            else:
                freq[j] = 1
    for key, value in freq.items():
        if value == x:
            newList += [key]
    return newList

print(fun([1,2,3], [2,3,4],[4,5,6], [4,1, "test"], x=2))
