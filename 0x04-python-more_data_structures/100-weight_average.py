#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    w = 0
    d = 0

    for x in my_list:
        w += x[0] * x[1]
        d += x[1]

    result = w / d

    return (result)
