import re

def function_4(xml_path,attrs, function):
    result = []
    with open(xml_path,"r") as f_d:
        for el in re.findall("<\w+.*?>",f_d.read()):
            if(all([re.search(item[0]+"\s*=\s*\""+item[1] + "\"",el,flags=re.I) for item in attrs.items()])):
                result+=[el]
    return result
