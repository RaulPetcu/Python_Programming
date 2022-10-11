def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fib_list(n):
    list = []
    while (n):
        list.append(fibonacci(n))
        n -= 1
    return list

n = int(input("Insert number: "))
print(fib_list(n))