#!/usr/bin/env python3

import fileinput

def elevator_iter(s):
    position = 0
    for c in s:
        if c == '(':
            position += 1
        if c == ')':
            position -= 1
        yield position

def elevator(s):
    return list(elevator_iter(s))[-1]

def when_floor(s, dest):
    if dest == 0:
        return 0
    return next((n + 1 for n, p in enumerate(elevator_iter(s)) if p == -1), None)

if __name__ == '__main__':
    s = ''
    for line in fileinput.input():
        s += line
    print("Final floor: %i" % elevator(s))
    print("Reach floor -1: %s" % when_floor(s, -1))
