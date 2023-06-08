#!/usr/bin/python3
import sys

args = len(sys.argv) - 1
i = 1

if __name__ == "__main__":
    if args < 1:
        print("0 arguments")
    elif args == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(args))
        for i in range(1, args + 1):
            print("{}: {}".format(i, sys.argv[i]))
