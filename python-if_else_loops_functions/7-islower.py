#!/usr/bin/python3
def islower(c):
    for i in range(97,123):
        if ord(c) == i:
           return "{} is lower".format(c)
    else:
        return "{} is upper".format(c)
print(islower('"'))
print(islower('a'))
print(islower('H'))
print(islower('4'))
print(islower('!'))
