#!/usr/bin/python3
i = 32
for c in range(90, 64, -1):
    print("{}".format(chr(c + i)), end='')
    if i == 0:
        i = 32
    else:
        i = 0
