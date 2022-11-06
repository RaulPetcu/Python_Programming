def func(pairs):
    res = []
    
    for pair in pairs:
        dict = {}
        dict["sum"] = pair[0] + pair[1]
        dict["prod"] = pair[0] * pair[1]
        dict["pow"] = pow(pair[0], pair[1])
        res.append(dict)
    
    return res

print(func(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))   