def sum_function(*args):
    s = 0
    for num in args:
        s += int(num)
    return s

lambda_sum = lambda *x : sum(x)

print(lambda_sum(1,23,3,2,2,2,2,2))

print(sum_function(1,1,1))

