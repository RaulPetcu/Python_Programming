def dict_check(dictionary):
    if type(dictionary) is not dict:
        return False
    else:
        if len(dictionary) < 2:
            return False
        else:
            flag = 0
            for key in dictionary.keys():
                if type(key) == str and len(key) > 2:
                    flag = 1
                    break
            if flag == 0:
                return False
            else:
                return True

def my_func(*args, **kwargs):
    dict_list = []

    for arg in args:
        if dict_check(arg):
            dict_list.append(arg)

    for kwarg in kwargs.values(): 
        if(dict_check(kwarg)):
            dict_list.append(kwarg)

    return dict_list

print(
    my_func(

 {1: 2, 3: 4, 5: 6}, 

 {'a': 5, 'b': 7, 'c': 'e'}, 

 {2: 3}, 

 [1, 2, 3],

 {'abc': 4, 'def': 5},

 3764,

 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

 test={1: 1, 'test': True}

)
)