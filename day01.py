#!/usr/bin/env python3

import fileinput

def elevator(s):
    return s.count('(') - s.count(')')

if __name__ == '__main__':
    s = ''
    for line in fileinput.input():
        s += line
    print("Final floor: %i" % elevator(s))
