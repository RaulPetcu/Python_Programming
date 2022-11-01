def func(dir_path):
    from os import listdir
    from os.path import isfile, join
    import os

    res = []

    onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    for f in onlyfiles:
        res. append(os.path.abspath(f))
    
    return res

print(func('/home/raul/dotnet'))