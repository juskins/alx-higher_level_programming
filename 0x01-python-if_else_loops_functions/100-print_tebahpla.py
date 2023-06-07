#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    if char % 2:
        print("{:c}".format((char - (ord('a') - ord('A')))), end="")
    else:
        print("{:c}".format(char), end="")
