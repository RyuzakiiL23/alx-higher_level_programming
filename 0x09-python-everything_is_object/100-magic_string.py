#!/usr/bin/python3
def magic_string():
    iteration = 1
    while True:
        yield ", ".join(["BestSchool"] * iteration)
        iteration += 1
