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

def dispatch_flight_path(s, count=1):
    loc = [(0, 0)] * count
    result = defaultdict(int)
    result[(0, 0)] += 1
    for i, c in enumerate(s):
        agent = i % count
        loc[agent] = move(loc[agent], c)
        result[loc[agent]] += 1
    return result

if __name__ == '__main__':
    s = ''
    for line in fileinput.input():
        s += line
    print("Flight path: %i" % len(dispatch_flight_path(s)))
    print("Santa + Robo-Santa flight path: %i" % len(dispatch_flight_path(s, 2)))
