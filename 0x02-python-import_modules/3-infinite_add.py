#!/usr/bin/python3
from sys import argv
sum_total = 0
for i in argv[1:]:
    sum_total += int(i)
print("{:d}".format(sum_total))
