def func(*argv):
    res = []
    # fac toate listele de aceiasi lungime
    max_len = 0
    for list in argv:
        if len(list) > max_len:
            max_len = len(list)
    for list in argv:
        if len(list) < max_len:
            howManyNone = max_len - len(list)
            while howManyNone > 0:
                list.append(None)
                howManyNone -= 1

    for i in range(max_len):
        my_tuple = ()
        for list in argv:
            my_tuple = my_tuple + (list[i],)
        res.append(my_tuple)

    return res


print(func([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
