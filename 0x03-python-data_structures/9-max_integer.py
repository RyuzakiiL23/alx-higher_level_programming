#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    else:
        x = my_list[0]
        i = 0
        while i < len(my_list):
            if x >= my_list[i]:
                i += 1
            else:
                x = my_list[i]
                i += 1

    return x
