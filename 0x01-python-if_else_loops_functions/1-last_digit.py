#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
cos = 0
if number >= 0:
    cos = number % 10
else:
    cos = number % -10
    print("Last digit of {:d} is {:d} and is ".format(number, cos), end = " ")
if cos > 5:
    print("greater than 5")
elif cos  == 0:
    print("0")
else:
    print ("less than 6 and not 0")

