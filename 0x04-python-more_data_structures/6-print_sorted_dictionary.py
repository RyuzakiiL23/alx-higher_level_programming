#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_list = list(a_dictionary.keys())
    sort_list.sort()
    for x in sort_list:
        print("{}: {}".format(x, a_dictionary.get(x)))
