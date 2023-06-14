#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    i = []
    for char in roman_string:
        if char in roman_values:
            i.append(roman_values[char])

    sum = 0
    len_i = len(i)
    for j in range(len_i):
        if j == 0:
            sum = i[j]
        elif i[j] <= i[j - 1]:
            sum += i[j]
        else:
            sum += i[j] - (i[j - 1] * 2)

    return sum
