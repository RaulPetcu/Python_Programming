def check_pal(number):
    aux = number
    invers = 0

    while aux != 0:
        invers = invers*10 + aux%10
        aux = aux // 10
    
    if invers == number:
        return "is palindrome"
    else:
        return "is not palindrome"

num = 123454321
print(check_pal(num))
