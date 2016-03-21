#!/usr/bin/env python3

import fileinput
import re

def is_nice(word):
    return bool(
        len(re.findall(r'[aeiou]', word)) >= 3 and
        re.search(r'([a-z])\1', word) and
        not re.search(r'ab|cd|pq|xy', word))

def is_naughty(word):
    return not is_nice(word)

if __name__ == '__main__':
    nice_count = 0
    for line in fileinput.input():
        line = line.strip()
        if is_nice(line):
            print(line)
            nice_count += 1
    print(nice_count)
