#!/usr/bin/python3
import hidden_4
for i in dir(hidden_4):
    if i[0:2] != "__":
        print("{:s}".format(i))