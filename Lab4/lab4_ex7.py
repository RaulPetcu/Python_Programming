def file_dict(filepath):
    import pathlib
    import os
    
    res = {}
    full_path = os.path.abspath(filepath)
    values = []
    size = os.stat(filepath).st_size
    extension = pathlib.Path(filepath).suffix[1:]
    f = open(full_path, 'a')
    writable = f.writable()
    f.close()
    f = open(full_path, 'r')
    readable = f.readable()
    f.close()

    res_values = [
        'file_size=' + str(size), 
        'file_extension=' + str(extension),
        'can_read=' + str(readable),
        'can_write=' + str(writable)
    ]

    res[full_path] = res_values

    return res

print(file_dict('/home/raul/Facultate/ANUL_3/Python/Lab2/lab2_ex2.py'))
