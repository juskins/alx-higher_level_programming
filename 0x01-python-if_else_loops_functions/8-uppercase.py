#!/usr/bin/python3
def isupper(str):
    for character in str:
        if ord('a') <= ord(character) <= ord('z'):
            character = chr(ord(character) - 32)
        print("{:s}".format(character), end="")
    print("")
