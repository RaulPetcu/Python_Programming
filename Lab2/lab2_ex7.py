def isPalindrome(num):
    inv = 0
    aux = num
    while(aux):
        inv = inv*10 + aux%10
        aux = aux // 10
    if inv == num:
        return True
    else:
        return False

def fun(numList):
    palindromeCount = 0
    palindromeMaxim = -320000
    for num in numList:
        if isPalindrome(num):
            palindromeCount += 1
            if num > palindromeMaxim:
                palindromeMaxim = num            
    return (palindromeCount, palindromeMaxim)

print(fun([121, 333333, 543, 3221, 898]))