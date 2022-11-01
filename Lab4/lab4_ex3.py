from genericpath import isdir


def func(my_path):
    import os
    # name = os.path.basename(my_path)

    if os.path.isfile(my_path):
        file = open(my_path, 'r')
        lines = file.read()
        return lines[-20]
    else:
        if os.path.isdir(my_path):
            from os import listdir
            import pathlib
            from os.path import isfile, join

            list_of_tuples = []
            freq_dict = {}
            onlyfiles = [f for f in listdir(
                my_path) if isfile(join(my_path, f))]
            for file in onlyfiles:
                file_extension = pathlib.Path(file).suffix
                if file_extension in freq_dict:
                    freq_dict[file_extension] += 1
                else:
                    freq_dict[file_extension] = 1

            for file_ext in freq_dict:
                list_of_tuples.append((file_ext, freq_dict[file_ext]))
            list_of_tuples.sort(key=lambda x: x[1])

            return list_of_tuples
        else:
            return 'Wrong path'


print(func('/home/raul/Facultate/ANUL_3/Python/Lab2'))
