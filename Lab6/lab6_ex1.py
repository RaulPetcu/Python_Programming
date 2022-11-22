import re
def extract_words(my_text):
    return re.findall("[a-z0-9]+",my_text,flags=re.IGNORECASE)
