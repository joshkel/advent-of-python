#!/usr/bin/python

from collections import defaultdict
import fileinput

dir = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0)
}

def move(start, c):
    return tuple(map(sum,zip(start, dir.get(c, (0, 0)))))

def flight_path(s):
    loc = (0, 0)
    result = defaultdict(int)
    result[loc] += 1
    for c in s:
        loc = move(loc, c)
        result[loc] += 1
    return result

if __name__ == '__main__':
    s = ''
    for line in fileinput.input():
        s += line
    print("Flight path: %i" % len(flight_path(s)))

    santa = s[::2]
    robo_santa = s[1::2]
    # NOTE: Resulting flight path's counts are wrong, but we only care about
    # number of locations visited
    result = flight_path(santa)
    result.update(flight_path(robo_santa))
    print("Santa + Robo-Santa flight path: %i" % len(result))
