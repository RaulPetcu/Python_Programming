import re
import os

def f(dir,regex):
    result = []

    for root,files in os.walk(dir):
        for f in files:
            file_name = os.path.join(root,f)
            reg = re.search(regex,f)
            if reg:
                result += [f]
            try:
                with open(file_name, "r") as f_d:
                        string = f_d.read()
                        if (re.search(regex, string)):
                            if reg:
                                result[-1] = "<<" + result[-1]
                            else:
                                result+=[f]
            except:
                pass
    return result