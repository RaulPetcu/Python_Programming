def func():
    import sys
    from os import listdir
    from os.path import isfile, join
    import pathlib

    for arg in sys.argv[1:]:
        dirpath = arg
        extensions = set()
        onlyfiles = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
        for file in onlyfiles:
            file_extension = pathlib.Path(file).suffix[1:]
            extensions.add(file_extension)
        # print(extensions)
        
    res = list(extensions)
    res.sort()
    return res

print(func())