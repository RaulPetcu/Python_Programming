def find_gcd(x, y):
     
    while(y):
        x, y = y, x % y
     
    return x

array = []
n = int(input("number of elements : "))
for i in range(0, n):
    num = int(input())
  
    array.append(num)
print(array)
         
num1 = array[0]
num2 = array[1]
gcd = find_gcd(num1, num2)
 
for i in range(2, len(array)):
    gcd = find_gcd(gcd, array[i])
     
print(gcd)