def my_func(list):
    res = []
    even_numbers = []
    odd_numbers = []
    for num in list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    for i in range(len(even_numbers)):
        res.append((even_numbers[i], odd_numbers[i]))

    return res

print(my_func([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

