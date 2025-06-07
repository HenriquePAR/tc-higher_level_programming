#!/usr/bin/python3
def islower(c):
    for i in range(97,123):
        if ord(c) == i:
           return "True"
    else:
        return "false"
print(islower('"'))
print(islower('a'))
print(islower('H'))
print(islower('4'))
print(islower('!'))
