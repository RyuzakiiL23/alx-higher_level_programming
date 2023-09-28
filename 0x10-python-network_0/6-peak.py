#!/usr/bin/python3
""" Def function find_peak """

def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None

    holder = list_of_integers[0]

    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] > holder:
            holder = list_of_integers[i]

    return holder

