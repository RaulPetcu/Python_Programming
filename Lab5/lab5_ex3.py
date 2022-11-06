def vowels_filter(s):
    res = []
    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u']:
            res.append(c)
    return res

string = "Programming in Python is fun."

string_list = [*string]

l1 = [c for c in string_list if c in ['a', 'e', 'i', 'o', 'u']]

l2 = list(filter(lambda c: c in ['a', 'e', 'i', 'o', 'u'], string_list))

l3 = vowels_filter(string_list)

print(l3)
