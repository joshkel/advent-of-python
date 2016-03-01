#!/usr/bin/env python3

import fileinput

def elevator(s):
    return s.count('(') - s.count(')')

def when_floor(s, dest):
    position = 0
    if dest == position:
        return 0
    for n, c in enumerate(s):
        if c == '(':
            position += 1
        if c == ')':
            position -= 1
        if position == dest:
            return n + 1
    return None

if __name__ == '__main__':
    s = ''
    for line in fileinput.input():
        s += line
    print("Final floor: %i" % elevator(s))
    print("Reach floor -1: %s" % when_floor(s, -1))
