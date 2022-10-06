string = input("Enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for s in string:
    if s in vowels:
        count += 1

print(count)