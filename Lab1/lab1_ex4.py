from curses.ascii import isupper


str = input("Enter a string in UpperCamelCase: ")
res = ""

res = [str[0].lower()]
for char in str[1:]:
    if char in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        res.append("_")
        res.append(char.lower())
    else:
        res.append(char.lower())
print(''.join(res))
