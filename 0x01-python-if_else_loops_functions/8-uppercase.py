#!/usr/bin/python3
def isupper(str):
    for character in str:
        if ord('a') <= ord(character) <= ord('z'):
            print("{:s}".format(chr(ord(character) - 32)), end="")
        else:
            print("{:s}".format(character), end="")
    print("")
