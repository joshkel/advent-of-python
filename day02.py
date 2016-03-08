#!/usr/bin/env python3

import fileinput

def parse_size(s):
    return tuple([int(value) for value in s.split('x')])

def wrapping_paper(size):
    a, b, c = sorted(size)
    return 3 * a * b + 2 * a * c + 2 * b * c

def ribbon(size):
    a, b, c = sorted(size)
    return 2 * a + 2 * b + a * b * c

if __name__ == '__main__':
    total_wrapping_paper = 0
    total_ribbon = 0
    for line in fileinput.input():
        size = parse_size(line)
        total_wrapping_paper += wrapping_paper(size)
        total_ribbon += ribbon(size)
    print("Total wrapping paper: %i" % total_wrapping_paper)
    print("Total ribbon: %i" % total_ribbon)
