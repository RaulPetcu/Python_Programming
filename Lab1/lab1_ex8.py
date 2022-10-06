number = 7

binary = str(bin(number))
print(binary)

count = 0
for b in binary:
    if b == "1":
        count += 1
print(count)