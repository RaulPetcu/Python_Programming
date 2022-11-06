def fib(n):
    res = []
    if (n > 0):
        f1, f2 = 0, 1
        if n == 1:
            print(f1)
        elif n == 2:
            print(f1, f2)
        else:            
            for i in range(1, n+1):
                f3 = f1 + f2
                res.append(f3)
                f1 = f2
                f2 = f3
    return res

def my_func(**kwargs):
    fib_list = fib(1000)

    for key, value in kwargs.items():
        if key == "filters":
            fib_list = list(filter(value, fib_list))
        if key == "limit":
            fib_list = list(filter(lambda x: x<=value, fib_list)) 
        if key == "offset":
            fib_list = fib_list[value:]
            

    return fib_list

print(my_func(
    filters=lambda item: item % 2 == 0,

    limit=300,

    offset=2
))
