#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_degit = number % 10
if number < 0:
    number = - number
    last_degit = number % 10
    last_degit = - last_degit
    number = - number
if last_degit > 5:
    print(f"Last digit of {number} is {last_degit} and is greater than 5")
elif last_degit == 0:
    print(f"Last digit of {number} is {last_degit} and is 0")
else:
    print(f"Last digit of {number} is {last_degit} and is less than 6 and not 0")
