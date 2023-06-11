#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tr_fal = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            tr_fal.append(True)
        else:
            tr_fal.append(False)
    return tr_fal
