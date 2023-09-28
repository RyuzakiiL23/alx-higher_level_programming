#!/usr/bin/python3
""" Def function find_peak """


def find_peak(list_of_integers):
    i = 0
    if len(list_of_integers) == 0:
        return None
    while i in range(len(list_of_integers) - 2):
        if (list_of_integers[i] >= list_of_integers[i+1]):
            holder = list_of_integers[i]
        else:
            holder = list_of_integers[i+1]
        i += 1
    return holder
