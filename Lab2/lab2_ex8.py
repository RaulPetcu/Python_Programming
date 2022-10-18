def divisibleBy(string_list, x=1, flag=True):
    big_list = []
    for string in string_list:
        l = []
        for c in string:
            if flag == True:
                if ord(c) % x == 0:
                    l.append(c)
            else:
                if ord(c) % x != 0:
                    l.append(c)

        if len(l) > 0:
            big_list.append(l)
    return big_list


print(divisibleBy(["test", "hello", "lab002"], 2, False))
