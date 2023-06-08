#!/usr/bin/python3
import sys
argv = sys.argv[1:]
args_num = len(argv)
result = 0
if __name__ == "__main__":
    for i in range(args_num):
        result += int(argv[i])
print("{}".format(result))
