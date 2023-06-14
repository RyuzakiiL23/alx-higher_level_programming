#!/ust/bit/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = list(a_dictionary.keys())
    sorted_keys.sort()
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
