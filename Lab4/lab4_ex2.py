def write_abs_path_to_file(dirpath, filepath):
    from os import listdir
    from os import path
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
    
    f = open(filepath, 'a')
    for file in onlyfiles:
        abs_path = path.abspath(file) 
        # if abs_path[0] == 'A':
        f.write(abs_path + '\n')
    f.close()

write_abs_path_to_file('/home/raul/Facultate/ANUL_3/Python/Lab2', '/home/raul/test/test.txt')

