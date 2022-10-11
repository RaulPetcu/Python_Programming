def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

def primeNumFromList(numList):    
    primeNumbers = []   
    for num in numList:
        if isPrime(num):
            primeNumbers.append(num)
    return primeNumbers

print(primeNumFromList([1,43,44,21,13,22,244,19]))