import re

def censorship(text):
    low_s = text.group(0).lower()
    if not (low_s[0] in "aeiou" and low_s[-1] in "aeiou"):
        return text.group(0)
    return "".join([ch if idx%2 == 0 else '*' for idx,ch in enumerate(text.group(0))])


def my_function(text):
    return re.sub("\w+",censorship,text)
