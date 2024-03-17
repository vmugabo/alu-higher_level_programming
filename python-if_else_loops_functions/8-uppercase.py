#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            letter = chr(ord(c) - 32)
        else:
            letter = c
        print("{}".format(letter), end="")
    print("")
