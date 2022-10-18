from curses import keyname


def order_string_tuples(tuples_list):
    tuples_list.sort(key= lambda c: c[1][2])

list = [("rew", "opop"), ("asd", "abc")];
print(list)
order_string_tuples(list)
print(list)