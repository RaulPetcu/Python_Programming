import re


def function_3(text_chars,regex_list):
    return [el for el in text_chars if any([re.search(r,el) for r in regex_list])]
