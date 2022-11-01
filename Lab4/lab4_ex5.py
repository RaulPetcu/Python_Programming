def search(target, to_search):
    import os

    if os.path.isdir(target):
        import glob
        res = []
        for file in glob.glob(target + '/**/*.txt', recursive=True):
            with open(file, 'r') as fp:
                lines = fp.readlines()
                for row in lines:
                    if row.find(to_search) != -1:
                        res.append(os.path.basename(file))
                        break
        return res
    else:
        if os.path.isfile(target):
            with open(target, "r") as fp:
                for line_number, line in enumerate(fp, start=1):  
                    if to_search in line:
                        return f"Word '{to_search}' found on line {line_number}"
        else:
            raise ValueError('Not a directory or file')


print(search('/home/raul/dotnet', 'ana'))
