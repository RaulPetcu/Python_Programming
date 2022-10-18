def dictDiff(d1, d2):
    result = []
    for key1, key2 in zip(d1,d2):
        if key1 != key2:
            result.append((key1, key2))
        if d1[key1] != d2[key2]:
            result.append((d1[key1], d2[key2]))
    return result

d1 = {'1' : '2', '2' : '34','3' : '11','4' : '67','5' : '5'}
d2 = {'7' : '2', '2' : '34','3' : '2','4' : '67','2' : '5',}

print(dictDiff(d1, d2))