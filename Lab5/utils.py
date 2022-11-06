def check_for_prime(x):
    if x == 1 or x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    
def process_item(x):
    while check_for_prime(x) == False:
        x += 1
    return x

user_input = input("Enter a number: ")
print(process_item(int(user_input)))