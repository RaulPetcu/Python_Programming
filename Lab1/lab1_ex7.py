from curses.ascii import isdigit


text = "An 23 apple is 123 USD"

number = ""
for c in text:
    if c.isdigit():
        number += c
    else:
        if number != "": # am terminat numarul
            break
print(number)

