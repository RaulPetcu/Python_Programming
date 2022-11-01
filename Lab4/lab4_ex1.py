from importlib.machinery import EXTENSION_SUFFIXES


def listExtensions(path):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    

    extensions = []
    for file in onlyfiles:
        ext = ''
        for c in reversed(file):
            if c != '.':
                ext += c
            else :
                break        
        extensions.append(ext[::-1]) # reversed
    
    extensions.sort()

    return set(extensions)

print(listExtensions('/home/raul/Facultate/ANUL_3/Python/Lab2'))
