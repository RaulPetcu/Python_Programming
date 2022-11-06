def find_numbers(list):
    res = []

    for element in list:
        if type(element) == int or type(element) == float:
            res.append(element)

    return res

print(find_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))