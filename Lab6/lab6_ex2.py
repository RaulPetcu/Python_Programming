import re

def function_2(regex_string,my_text,x):
    return list(filter(lambda el:len(el)==x, re.findall(regex_string,my_text)))
